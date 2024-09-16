from typing import Annotated
from fastapi import APIRouter, Body
from notifications import (
    manager,
)

router = APIRouter()


@router.post("/")
async def send_custom_notification(message: Annotated[dict, Body()]):
    await manager.broadcast(message)
    return message
