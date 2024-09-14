from enum import Enum as PyEnum

from sqlalchemy import Column, String
from sqlalchemy.orm import (DeclarativeBase, Mapped, declared_attr,
                            mapped_column)


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)


class TaskStatus(PyEnum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"


class Device(Base):
    name = Column(String, index=True)
    online: Mapped[bool] = mapped_column(default=False)


class Task(Base):
    name: Mapped[str] = mapped_column(String, index=True)
    status: Mapped[TaskStatus] = mapped_column(default=TaskStatus.pending)
