from sqlalchemy.orm import Session
from app.models import Equa
from app.schemas import EquaSchema


def get_equa(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Equa).offset(skip).limit(limit).all()


# def get_book_by_id(db: Session, book_id: int):
#     return db.query(Equa).filter(Equa.id == book_id).first()


def create_equa(db: Session, equa: EquaSchema):
    _equa = Equa(function=equa.function, equation=equa.equation)
    db.add(_equa)
    db.commit()
    db.refresh(_equa)
    return _equa


# def remove_book(db: Session, book_id: int):
#     _book = get_book_by_id(db=db, book_id=book_id)
#     db.delete(_book)
#     db.commit()


# def update_book(db: Session, book_id: int, title: str, description: str):
#     _book = get_book_by_id(db=db, book_id=book_id)

#     _book.title = title
#     _book.description = description

#     db.commit()
#     db.refresh(_book)
#     return _book
