from fastapi import HTTPException
from sqlalchemy.orm import Session

import schemas
from models import Book


def create_book(book_scheme: schemas.BookBase, db: Session) -> schemas.Book:
    book_model = Book(**book_scheme.model_dump())
    db.add(book_model)
    db.commit()
    db.refresh(book_model)

    return book_model


def get_all_books(db: Session) -> list[schemas.Book]:
    return db.query(Book).all()


def get_book_by_id(pk: int, db: Session) -> schemas.Book | None:
    return db.query(Book).filter(Book.id == pk).first()


def get_book_or_404(pk: int, db: Session) -> schemas.Book:
    book = get_book_by_id(pk, db)
    if not book:
        raise HTTPException(404, f"Book with id {pk} is yet to be born(((")
    return book


def update_book(book: Book, book_schema: schemas.BookBase, db: Session) -> schemas.Book:
    book.title = book_schema.title
    book.author = book_schema.author
    book.genre = book_schema.genre
    book.publication_year = book_schema.publication_year

    db.commit()
    db.refresh(book)
    return book


def delete_book(book: Book, db: Session) -> dict[str, bool]:
    db.delete(book)
    db.commit()
    return {"ok": True}
