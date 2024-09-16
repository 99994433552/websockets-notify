import json
import random
from datetime import datetime
from uuid import uuid4

from fastapi import WebSocket


# Function to create notification message
def create_notification_message(
    message: str, url: str, msg_type: str = "INFO"
) -> dict:
    return {
        "id": str(uuid4()),
        "message": message,
        "url": url,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "type": msg_type,
    }


# Function to generate a random URL
def generate_random_url(item_id: int, prefix: str = "tasks") -> str:
    valid_domain = "localhost:3000"
    invalid_domains = [
        "invalid_domain.com",
        "no-such-site.xyz",
        "random-string-123",
        "error-url.test",
        "wrongdomain.invalid",
    ]
    domain = (
        valid_domain
        if random.random() < 0.8
        else random.choice(invalid_domains)
    )
    return f"http://{domain}/{prefix}/{item_id}"


# WebSocket manager
class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        message_json = json.dumps(message)
        for connection in self.active_connections:
            await connection.send_text(message_json)

    async def broadcast_plain(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()
