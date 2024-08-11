from pydantic import BaseModel, PositiveInt, ConfigDict


class BookBase(BaseModel):
    title: str
    author: str
    genre: str
    publication_year: PositiveInt


class Book(BookBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
