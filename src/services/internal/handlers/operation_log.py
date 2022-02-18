from src.adapters.repositories.operation_log.firestore import FirestoreOperationLogRepository
from src.factories.operation_log import build_operation_log_from_command
from src.adapters.repositories.operation_log.ports import OperationLogRepository
from src.services.internal.commands.operation_log import CreateOperationLogCommand


def create_operation_log(
    command: CreateOperationLogCommand,
    repository: OperationLogRepository = FirestoreOperationLogRepository()
):
    operation_log = build_operation_log_from_command(command)
    return repository.add(operation_log)
