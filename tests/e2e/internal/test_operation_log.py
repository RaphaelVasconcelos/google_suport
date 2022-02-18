from unittest import mock

import pytest

from src.entrypoints.http.handlers.internal_base_handler import THERE_IS_NO_MESSAGE_TO_PROCCESS


@pytest.mark.usefixtures('mock_operation_log_repository_in_create_operation_log')
def test_it_should_persist_operation_log(pubsub_message_body, http_cli):
    response = http_cli.post('/internal/operation-log/', json=pubsub_message_body)
    assert response.status_code == 200
    assert isinstance(response.json['operation_log_id'], str)


def test_it_should_return_response_without_persist_operation_log(http_cli, pubsub_message_body_with_empty_side_effects):
    path = 'src.entrypoints.http.handlers.internal.operation_log.create_operation_log'
    with mock.patch(path) as mocked_create_operation_log:
        response = http_cli.post('/internal/operation-log/', json=pubsub_message_body_with_empty_side_effects)
    assert mocked_create_operation_log.mock_calls == []
    assert response.status_code == THERE_IS_NO_MESSAGE_TO_PROCCESS
