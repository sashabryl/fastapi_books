from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException
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


@app.get("/books/{pk}/", response_model=schemas.Book)
def get_book_bY_id(pk: int, db: Session = Depends(get_db)) -> schemas.Book:
    book = crud.get_book_or_404(pk, db)

    return book


@app.put("/books/{pk}/", response_model=schemas.Book)
def update_book(
    pk: int,
    book_schema: Annotated[schemas.BookBase, Depends()],
    db: Session = Depends(get_db)
) -> schemas.Book:
    book = crud.get_book_or_404(pk, db)

    return crud.update_book(book, book_schema, db)


@app.delete("/books/{pk}/")
def delete_book(pk: int, db: Session = Depends(get_db)) -> dict[str, bool]:
    book = crud.get_book_or_404(pk, db)
    return crud.delete_book(book, db)
