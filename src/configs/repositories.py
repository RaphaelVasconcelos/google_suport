import os
from dataclasses import dataclass


@dataclass
class OperationLogRepositoryConfig:
    collection: str = os.environ['OPERATION_LOG_COLLECTION']


@dataclass
class OperationLogRepositoryTestsConfig(OperationLogRepositoryConfig):
    collection: str = 'operation-log-test'
