from datetime import datetime

from pydantic import BaseModel


class CreateOperationLogCommand(BaseModel):
    object_id: str
    client_id: str
    client_id_source: str
    action: str
    action_data: dict
    reason: str
    metadata: dict
    request_date: datetime
    email: str
