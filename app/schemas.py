from pydantic import BaseModel

from models import TaskStatus


class Device(BaseModel):
    id: int
    name: str
    online: bool


class TaskBase(BaseModel):
    name: str
    status: TaskStatus


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
