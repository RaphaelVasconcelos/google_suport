from google.api_core.exceptions import AlreadyExists
from google.cloud import firestore

from src.adapters.repositories.operation_log.ports import OperationLogRepository
from src.configs.repositories import OperationLogRepositoryConfig
from src.exceptions.operation_log import OperationLogError
from src.factories.operation_log import build_operation_log_from_dict
from src.models.operation_log import OperationLog


class FirestoreOperationLogRepository(OperationLogRepository):

    def __init__(self, configs: OperationLogRepositoryConfig = OperationLogRepositoryConfig()):
        self._collection = firestore.Client().collection(configs.collection)
        self._configs = configs

    def _uid_to_string(self, operation_log_doc):
        operation_log_doc['uid'] = str(operation_log_doc['uid'])

    def _add(self, operation_log: OperationLog):
        doc_ref = self._collection.document(str(operation_log.uid))
        operation_log_doc = operation_log.dict()
        self._uid_to_string(operation_log_doc)
        try:
            doc_ref.create(operation_log_doc)
        except AlreadyExists:
            raise OperationLogError(f'OperationLog already exists: {operation_log}')
        return operation_log

    def _build_operation_log(self, doc):
        operation_log_data = doc.to_dict()
        operation_log_data['request_date'] = operation_log_data['request_date'].isoformat()
        operation_log_data['created_at'] = operation_log_data['created_at'].isoformat()
        return build_operation_log_from_dict(operation_log_data)

    def filter(self, object_id: str) -> list[OperationLog]:
        query = self._collection.where('object_id', '==', object_id).order_by('request_date', 'DESCENDING')
        operations_logs = [self._build_operation_log(operation_log) for operation_log in query.get()]
        return operations_logs
