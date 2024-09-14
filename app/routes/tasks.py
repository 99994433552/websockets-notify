from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db
from models import TaskStatus
from notifications import (
    create_notification_message,
    generate_random_url,
    manager,
)

router = APIRouter()


@router.get("/", response_model=list[schemas.Task])
async def read_tasks(db: Session = Depends(get_db)):
    return crud.read_tasks(db)


@router.post("/", response_model=schemas.Task)
async def create_task(
    data: schemas.TaskCreate,
    db: Session = Depends(get_db),
):
    task = crud.create_task(db, data)

    message = create_notification_message(
        message=f"New task {task.name} created",
        url=generate_random_url(task.id),
        msg_type="SUCCESS",
    )
    await manager.broadcast(message)
    return task


@router.put("/{task_id}", response_model=schemas.Task)
async def update_task_status(
    task_id: int, status: TaskStatus, db: Session = Depends(get_db)
):
    task = crud.read_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    updated_task = crud.update_task_status(db, task, status)

    message = create_notification_message(
        message=f"Task {updated_task.id} status updated to {updated_task.status.value}",
        url=generate_random_url(updated_task.id),
        msg_type="SUCCESS",
    )

    await manager.broadcast(message)
    return updated_task


@router.delete("/{task_id}", response_model=schemas.Task)
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.read_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    deleted_task = crud.delete_task(db, task)

    message = create_notification_message(
        message=f"Task {deleted_task.name} deleted",
        url=generate_random_url(deleted_task.id),
        msg_type="ALERT",
    )
    await manager.broadcast(message)
    return deleted_task
