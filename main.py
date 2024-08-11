from typing import Annotated

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import schemas
import crud
from dependencies import get_db

app = FastAPI(root_path="/api")


@app.post("/books/", response_model=schemas.Book)
def create_book(
    book_schema: Annotated[schemas.BookBase, Depends()],
    db: Session = Depends(get_db)
) -> schemas.Book:
    return crud.create_book(book_schema, db)


@app.get("/books/", response_model=list[schemas.Book])
def get_all_books(db: Session = Depends(get_db)) -> list[schemas.Book]:
    return crud.get_all_books(db)
