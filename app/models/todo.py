from sqlalchemy.sql.sqltypes import Integer
from app.db.connection import Base
from sqlalchemy import Column, String, Boolean


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), index=True)
    done = Column(Boolean, default=False)
