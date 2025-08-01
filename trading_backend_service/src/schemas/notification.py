from typing import List
from pydantic import BaseModel

# PUBLIC_INTERFACE
class Notification(BaseModel):
    id: str
    type: str
    content: str
    read: bool

# PUBLIC_INTERFACE
class SendNotificationRequest(BaseModel):
    user_id: str
    content: str
    type: str

# PUBLIC_INTERFACE
class NotificationListResponse(BaseModel):
    notifications: List[Notification]
