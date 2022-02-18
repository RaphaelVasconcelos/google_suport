import uuid
from datetime import datetime

from src.services.internal.commands.operation_log import CreateOperationLogCommand
from src.models.operation_log import OperationLog


def build_operation_log_from_dict(data: dict):
    return OperationLog.parse_obj(data)


def build_operation_log_from_command(command: CreateOperationLogCommand):
    return OperationLog(
        uid=uuid.uuid4(),
        object_id=command.object_id,
        client_id=command.client_id,
        client_id_source=command.client_id_source,
        action=command.action,
        action_data=command.action_data,
        reason=command.reason,
        metadata=command.metadata,
        email=command.email,
        request_date=command.request_date,
    )


def build_a_create_operation_log_command(
    object_id: str,
    client_id: str,
    client_id_source_value: str,
    action_value: str,
    action_data: dict,
    reason: str,
    metadata: dict,
    email: str,
    request_date: datetime
):
    return CreateOperationLogCommand(
        object_id=object_id,
        client_id=client_id,
        client_id_source=client_id_source_value,
        action=action_value,
        action_data=action_data,
        reason=reason,
        metadata=metadata,
        request_date=request_date,
        email=email,
    )
