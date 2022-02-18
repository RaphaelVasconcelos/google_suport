import uuid

from src.factories.operation_log import build_operation_log_from_command
from src.services.internal.commands.operation_log import CreateOperationLogCommand


def test_if_uid_is_being_populated(operation_log: CreateOperationLogCommand):
    create_operation_log = CreateOperationLogCommand(
        object_id=operation_log.object_id,
        client_id=operation_log.client_id,
        client_id_source=operation_log.client_id_source,
        action=operation_log.action,
        action_data=operation_log.action_data,
        reason=operation_log.reason,
        metadata=operation_log.metadata,
        request_date=operation_log.request_date,
        email=operation_log.email,
    )
    except_result = build_operation_log_from_command(create_operation_log)
    assert isinstance(except_result.uid, uuid.UUID)
