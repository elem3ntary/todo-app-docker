from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB

CONNECTION_STRING = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}?charset=utf8mb4"

# CONNECTION_STRING = "sqlite:///./app.db"
engine = create_engine(CONNECTION_STRING)
Base = declarative_base(bind=engine)

SessionLocal = sessionmaker(bind=engine)
