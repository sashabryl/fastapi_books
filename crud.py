from sqlalchemy.orm import Session

import schemas
from models import Book


def create_book(book_scheme: schemas.BookBase, db: Session):
    book_model = Book(**book_scheme.model_dump())
    db.add(book_model)
    db.commit()
    db.refresh(book_model)

    return book_model