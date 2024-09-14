import asyncio

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from database import engine, get_db
from models import Base
from notifications import manager
from routes import devices, tasks, notify
from services import background_device_status_update, initialize_fake_data

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.on_event("startup")
async def startup_event():
    db = next(get_db())
    initialize_fake_data(db)
    asyncio.create_task(background_device_status_update(db))


# WebSocket route
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)


app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
app.include_router(devices.router, prefix="/devices", tags=["Devices"])
app.include_router(notify.router, prefix="/notify", tags=["Notify"])
