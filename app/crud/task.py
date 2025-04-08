from sqlmodel import Session, select
from app.db.models import Task
from typing import List, Optional
from datetime import datetime
from sqlalchemy.sql import or_

def create_task(session: Session, user_id: int, title: str, description: Optional[str]) -> Task:
    task = Task(title=title, description=description, user_id=user_id)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def get_tasks(session: Session, user_id: int, query: Optional[str] = None, date: Optional[str] = None) -> List[Task]:
    statement = select(Task).where(Task.user_id == user_id, Task.is_deleted == False)
    if query:
        statement = statement.where(or_(Task.title.ilike(f"%{query}%"), Task.description.ilike(f"%{query}%")))
    if date:
        statement = statement.where(Task.timestamp.cast("date") == date)
    return session.exec(statement).all()

def get_task(session: Session, user_id: int, task_id: int) -> Optional[Task]:
    return session.exec(select(Task).where(Task.id == task_id, Task.user_id == user_id, Task.is_deleted == False)).first()

def update_task(session: Session, task: Task, title: str, description: Optional[str]) -> Task:
    task.title = title
    task.description = description
    task.timestamp = datetime.utcnow()
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def soft_delete_task(session: Session, task: Task):
    task.is_deleted = True
    session.add(task)
    session.commit()
