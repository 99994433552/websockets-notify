import asyncio
import random

from sqlalchemy.orm import Session

from models import Device, Task
from notifications import (
    create_notification_message,
    manager,
    generate_random_url,
)


# Background task for randomly updating device status
async def background_device_status_update(db: Session):
    while True:
        await asyncio.sleep(random.randint(1, 60))
        devices = db.query(Device).all()
        if devices:
            device = random.choice(devices)
            device.online = not device.online
            db.commit()

            message = create_notification_message(
                message=f"Device {device.name} is now {'online' if device.online else 'offline'}",
                url=generate_random_url(prefix="devices", item_id=device.id),
                msg_type="INFO" if device.online else "ALERT",
            )
            await manager.broadcast(message)


# Function to initialize devices and tasks during startup
def initialize_fake_data(db: Session):
    if db.query(Device).count() == 0:
        devices = [Device(name=f"Device U{i}") for i in range(1, 11)]
        db.add_all(devices)
        db.commit()
    if db.query(Task).count() == 0:
        tasks = [Task(name=f"Task U{i}") for i in range(1, 11)]
        db.add_all(tasks)
        db.commit()
