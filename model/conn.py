
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

env = os.getenv("env", "test")

# 데이터베이스 연결 설정

DATABASE_URL = "sqlite:///./test.db"

if env == "test":
    DATABASE_URL = "sqlite:///./test.db"
elif env == "dev":
    DATABASE_URL = "sqlite:///./dev.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()

# Session 생성
Session = sessionmaker(bind=engine)
session = Session()