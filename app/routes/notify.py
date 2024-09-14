from fastapi import APIRouter
from notifications import (
    manager,
)

router = APIRouter()


@router.post("/")
async def send_custom_notification(message: str):
    await manager.broadcast_plain(message)
    return {"message": "Notification sent"}
