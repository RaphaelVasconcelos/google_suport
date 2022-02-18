from src.services.internal.commands.operation_log import CreateOperationLogCommand
from src.services.internal.handlers.operation_log import create_operation_log
from tests.unit.services.fakes import FakeOperationLogRepository


def test_it_should_persist_the_operation_log(operation_log):
    command = CreateOperationLogCommand(
        object_id=operation_log.object_id,
        client_id=operation_log.client_id,
        client_id_source=operation_log.client_id_source,
        action=operation_log.action,
        action_data=operation_log.action_data,
        reason=operation_log.reason,
        metadata=operation_log.metadata,
        request_date=operation_log.request_date,
        email='',
    )
    repository = FakeOperationLogRepository()
    create_operation_log(command, repository)
    assert len(repository.logs) == 1
