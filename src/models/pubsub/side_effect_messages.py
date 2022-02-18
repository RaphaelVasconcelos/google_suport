from datetime import datetime

from pydantic import BaseModel

from src.services.internal.commands.operation_log import CreateOperationLogCommand


class SideEffectMessage(BaseModel):

    def dict(self, *args, **kwargs):
        dictonary = super().dict(*args, **kwargs)
        dictonary_copy = dict(dictonary)
        for key, value in dictonary_copy.items():
            if isinstance(value, datetime):
                dictonary[key] = value.isoformat()
        return dictonary


class OperationLogSideEffectMessage(SideEffectMessage, CreateOperationLogCommand):
    pass
