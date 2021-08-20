from app.schemas.todo import TodoUpdate
from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm.session import Session
from app.db.base import Base
from app.db.connection import SessionLocal
from app.crud.todo import get_many_todos, create_todo, delete_todo, update_todo
from app.schemas import TodoBase, TodoCreate, TodoUpdate

Base.metadata.create_all()

app = FastAPI()

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()


@app.get("/", response_model=List[TodoBase])
def get(db: Session = Depends(get_db)):
    todos = get_many_todos(db)
    return todos


@app.post("/", response_model=TodoBase)
def post(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = create_todo(db, todo)
    return db_todo


@app.put("/{todo_id}")
def put(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    return update_todo(db, todo_id, todo)


@app.delete("/{todo_id}")
def delete(todo_id: int, db: Session = Depends(get_db)):
    return delete_todo(db, todo_id)
