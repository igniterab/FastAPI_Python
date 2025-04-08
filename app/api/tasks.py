from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List, Optional
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut
from app.db.database import get_session
from app.dependencies.deps import get_current_user
from app.db.models import User
from app.crud import task as crud_task

router = APIRouter()

@router.post("/", response_model=TaskOut)
def create_task(task: TaskCreate, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    return crud_task.create_task(session, current_user.id, task.title, task.description)

@router.get("/", response_model=List[TaskOut])
def list_tasks(query: Optional[str] = None, date: Optional[str] = None, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    return crud_task.get_tasks(session, current_user.id, query, date)

@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    task = crud_task.get_task(session, current_user.id, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskOut)
def update_task(task_id: int, updated: TaskUpdate, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    task = crud_task.get_task(session, current_user.id, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return crud_task.update_task(session, task, updated.title, updated.description)

@router.delete("/{task_id}")
def delete_task(task_id: int, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    task = crud_task.get_task(session, current_user.id, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    crud_task.soft_delete_task(session, task)
    return {"detail": "Task deleted"}