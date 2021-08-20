from app.models import Todo
from sqlalchemy.orm import Session
from app.schemas import TodoCreate, TodoUpdate


def get_many_todos(db: Session):
    return db.query(Todo).all()


def create_todo(db: Session, todo: TodoCreate):
    db_todo = Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    return db_todo


def delete_todo(db: Session, todo_id: int):
    result = db.query(Todo).filter_by(id=todo_id).delete()
    return bool(result)


def update_todo(db: Session, todo_id: int, todo: TodoUpdate):
    result = db.query(Todo).filter_by(id=todo_id).update(todo.dict())
    return bool(result)
