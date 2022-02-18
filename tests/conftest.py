import base64
from datetime import datetime

import pytest
from google.cloud import firestore

from src.adapters.repositories.operation_log.firestore import FirestoreOperationLogRepository
from src.configs.repositories import OperationLogRepositoryTestsConfig
from src.entrypoints.http.server import create_app
from src.factories.operation_log import build_operation_log_from_command

from src.services.internal.commands.operation_log import CreateOperationLogCommand


def _clean_collection(collection_path, client=firestore.Client()):
    documents = client.collection(collection_path).list_documents()
    for document in documents:
        for collection in document.collections():
            _clean_collection('/'.join(collection._path), client=client)
        document.delete()


@pytest.fixture
def operation_log_repository():
    operation_log_repository_config = OperationLogRepositoryTestsConfig()
    _clean_collection(operation_log_repository_config.collection)
    return FirestoreOperationLogRepository(configs=operation_log_repository_config)


@pytest.fixture
def operation_log():
    return build_operation_log_from_command(
        CreateOperationLogCommand(
            object_id="object.id",
            client_id='auth0|USER-ID',
            client_id_source="AUTH0",
            action="Do Something",
            action_data={'blocked_balance_amount': 100},
            reason='dummy_reason',
            email='test@email.com',
            metadata={'dummy_key': 'dummy_value'},
            request_date=datetime.fromisoformat('2021-06-30T12:02:37.471000+00:00'),
        )
    )


@pytest.fixture
def pubsub_message_body():
    pubsub_message_json = (
        '{"side_effect_messages": [{"object_id": "cp_123", "client_id": "auth0|USER-ID", '
        '"client_id_source": "auth0_client_id_from_sub_claim", '
        '"action": "change_object_blocked_balance_amount", '
        '"action_data": {"object_id": "cp_123", "blocked_balance_amount": 100000000000}, "reason": "dummy_reason", '
        '"metadata": {"dummy_key": "dummy_value"}, "request_date": "2022-02-14T12:42:48.007243+00:00", '
        '"email": "test@email.com"}, {"object_id": "cp_123", "content": "dummy_reason", "action": '
        '"change_object_blocked_balance_amount", '
        '"action_data": {"object_id": "cp_123", "blocked_balance_amount": 100000000000}}, {"object_id": "cp_123", '
        '"action": "change_object_blocked_balance_amount", "action_data": {"object_id": "cp_123", "blocked_balance_amount": 100000000000}}]}'
    )

    return {
        'message': {
            'attributes': {
                'correlation_id': 'dummy_correlation_id',
            },
            'data': base64.b64encode(pubsub_message_json.encode('utf-8')).decode('utf-8'),
            'messageId': '2070443601311540',
            'message_id': '2070443601311540',
            'publishTime': '2021-02-26T19:13:55.749Z',
            'publish_time': '2021-02-26T19:13:55.749Z',
        },
        'subscription': 'projects/myproject/subscriptions/mysubscription'
    }


@pytest.fixture
def pubsub_message_body_with_empty_side_effects():
    pubsub_message_json = '{"side_effect_messages": []}'
    return {
        'message': {
            'attributes': {
                'correlation_id': 'dummy_correlation_id',
            },
            'data': base64.b64encode(pubsub_message_json.encode('utf-8')).decode('utf-8'),
            'messageId': '2070443601311540',
            'message_id': '2070443601311540',
            'publishTime': '2021-02-26T19:13:55.749Z',
            'publish_time': '2021-02-26T19:13:55.749Z',
        },
        'subscription': 'projects/myproject/subscriptions/mysubscription'
    }


@pytest.fixture
def flask_app():
    app = create_app()
    app.config.update({'PROPAGATE_EXCEPTIONS': False})
    return app
