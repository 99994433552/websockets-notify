from sqlalchemy.orm import Session

from models import Device, Task, TaskStatus
from schemas import TaskCreate


def read_devices(db: Session):
    return db.query(Device).all()


def create_task(db: Session, task: TaskCreate) -> Task:
    task_dict = task.model_dump()
    model_data = Task(**task_dict)
    db.add(model_data)
    db.commit()
    db.refresh(model_data)
    return model_data


def read_tasks(db: Session):
    return db.query(Task).all()


def read_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def update_task_status(db: Session, task: Task, status: TaskStatus):
    task.status = status
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task: Task):
    db.delete(task)
    db.commit()
    return task
