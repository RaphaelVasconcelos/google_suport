import abc
from datetime import datetime, timezone

from src.models.operation_log import OperationLog


class OperationLogRepository(abc.ABC):

    def _set_time(self, operation_log):
        operation_log.created_at = datetime.now(timezone.utc)

    def add(self, operation_log: OperationLog) -> OperationLog:
        self._set_time(operation_log)
        return self._add(operation_log)

    @abc.abstractmethod
    def _add(self, operation_log: OperationLog) -> OperationLog:
        pass

    @abc.abstractmethod
    def filter(self, object_id: str) -> list[OperationLog]:
        pass
