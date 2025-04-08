from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True