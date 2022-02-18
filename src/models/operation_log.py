import uuid
from datetime import datetime

from pydantic.main import BaseModel


class OperationLog(BaseModel):
    uid: uuid.UUID
    object_id: str
    client_id: str
    client_id_source: str
    action: str
    action_data: dict
    reason: str
    metadata: dict
    email: str
    request_date: datetime
    created_at: datetime = None
