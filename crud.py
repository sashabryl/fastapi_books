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
