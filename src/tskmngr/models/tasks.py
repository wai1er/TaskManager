from datetime import date

from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: str
    deadline: date
    assigned_to: str
    status: str


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass
