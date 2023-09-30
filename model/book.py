from sqlalchemy import Column, Integer, String
from model.conn import Base

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255))
    author = Column(String(255))
    year = Column(Integer)

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year