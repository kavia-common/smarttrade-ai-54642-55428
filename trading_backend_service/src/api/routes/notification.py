from fastapi import APIRouter
from src.schemas.notification import SendNotificationRequest, NotificationListResponse, Notification

router = APIRouter(
    prefix="/api/notifications",
    tags=["Notifications"]
)

# PUBLIC_INTERFACE
@router.get("/", response_model=NotificationListResponse, summary="List notifications", description="Get all user notifications.")
async def get_notifications():
    return NotificationListResponse(notifications=[
        Notification(id="n1", type="news", content="Welcome!", read=False)
    ])

# PUBLIC_INTERFACE
@router.post("/send", summary="Send notification", description="Send a notification to a user.")
async def send_notification(payload: SendNotificationRequest):
    return {"detail": "Notification sent"}

# PUBLIC_INTERFACE
@router.get("/websocket-doc", summary="WebSocket notifications usage", description="WebSocket for notifications: Connect to ws://host/ws/notifications for real-time alerts.", tags=["WebSocket"])
async def websocket_doc():
    return {
        "info": "Connect to ws://host/ws/notifications with access token query param for real-time alerts."
    }
