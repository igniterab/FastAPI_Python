from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    is_deleted: bool = Field(default=False)

    user_id: int = Field(foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="tasks")

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    hashed_password: str

    tasks: List[Task] = Relationship(back_populates="user")