from unittest import mock
import pytest
from contextlib import contextmanager

from src.services.internal.handlers.operation_log import create_operation_log


@pytest.fixture
def http_cli(flask_app):
    with flask_app.test_client() as client:
        yield client


@contextmanager
def _mock_operation_log_repository_in_create_operation_log(operation_log_repository):
    default_parameters = list(create_operation_log.__defaults__)
    default_parameters[0] = operation_log_repository
    with mock.patch.object(
        create_operation_log,
        '__defaults__',
        tuple(default_parameters),
    ):
        yield


@pytest.fixture
def mock_operation_log_repository_in_create_operation_log(operation_log_repository):
    with _mock_operation_log_repository_in_create_operation_log(operation_log_repository):
        yield
