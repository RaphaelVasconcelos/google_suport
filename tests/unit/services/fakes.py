from src.adapters.repositories.operation_log.ports import OperationLogRepository

from src.models.operation_log import OperationLog


class FakeOperationLogRepository(OperationLogRepository):
    def __init__(self):
        self.logs = []

    def _add(self, operation_log):
        self.logs.append(operation_log)

    def filter(self, object_id: str) -> list[OperationLog]:
        pass
