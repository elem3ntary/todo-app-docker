from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str


class TodoUpdate(TodoCreate):
    done: bool


class TodoBase(TodoUpdate):
    id: int

    class Config:
        orm_mode = True
