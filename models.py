from sqlalchemy import Column, Integer, String

from database import Base


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    author = Column(String(255))
    genre = Column(String(255))
    publication_year = Column(Integer)
