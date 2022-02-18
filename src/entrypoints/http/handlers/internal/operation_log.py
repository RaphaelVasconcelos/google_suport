from datetime import datetime

import flask

from src.entrypoints.http.handlers.internal_base_handler import InternalBaseView
from src.factories.operation_log import build_a_create_operation_log_command
from src.services.internal.commands.operation_log import CreateOperationLogCommand
from src.services.internal.handlers.operation_log import create_operation_log


class CreateOperationLogView(InternalBaseView):

    command = CreateOperationLogCommand

    def _handle_request(self, side_effect_message_data):
        side_effect_message_data['request_date'] = datetime.fromisoformat(side_effect_message_data['request_date'])
        command = build_a_create_operation_log_command(
            object_id=side_effect_message_data['object_id'],
            client_id=side_effect_message_data['client_id'],
            client_id_source_value=side_effect_message_data['client_id_source'],
            action_value=side_effect_message_data['action'],
            action_data=side_effect_message_data['action_data'],
            reason=side_effect_message_data['reason'],
            metadata=side_effect_message_data['metadata'],
            request_date=side_effect_message_data['request_date'],
            email=side_effect_message_data['email'],
        )
        operation_log = create_operation_log(command)
        return flask.jsonify({'operation_log_id': operation_log.uid}), 200
