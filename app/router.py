from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from datetime import datetime

from app.database import get_session
from app.schema import Todo, TodoCreate, TodoUpdate, TodoResponse

router = APIRouter(prefix="/todos", tags=["todos"])

@router.get("/", response_model=List[TodoResponse])
def get_todos(session: Session = Depends(get_session)):
    """Get all todos"""
    todos = session.exec(select(Todo)).all()
    return todos

@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, session: Session = Depends(get_session)):
    """Get a specific todo by ID"""
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.post("/", response_model=TodoResponse)
def create_todo(todo: TodoCreate, session: Session = Depends(get_session)):
    """Create a new todo"""
    db_todo = Todo.model_validate(todo)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo_update: TodoUpdate, session: Session = Depends(get_session)):
    """Update a todo"""
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todo_data = todo_update.model_dump(exclude_unset=True)
    if todo_data:
        todo_data["updated_at"] = datetime.now()
        for field, value in todo_data.items():
            setattr(todo, field, value)
        
        session.add(todo)
        session.commit()
        session.refresh(todo)
    
    return todo

@router.delete("/{todo_id}")
def delete_todo(todo_id: int, session: Session = Depends(get_session)):
    """Delete a todo"""
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    session.delete(todo)
    session.commit()
    return {"message": "Todo deleted successfully"}