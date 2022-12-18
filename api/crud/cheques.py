from sqlalchemy.orm import Session

from core.db.models import Cheque
from crud.persons import get_person_by_name, create_person
from crud.positions import create_position
from schemas.models import Position
from typing import List


def create_cheque(db: Session, name: str, payer_name: str, positions: [Position]) -> Cheque:
    payer_db = get_person_by_name(db, payer_name)
    if payer_db is None:
        payer_db = create_person(db, payer_name)
    cheque_db = Cheque(
        name=name,
        payer_id=payer_db.id,
        positions=[create_position(db, e.name, e.cost, e.owner.name, ) for e in positions],
    )
    db.add(cheque_db)
    db.commit()
    return cheque_db


def get_cheque_by_id(db: Session, id: int) -> Cheque:
    cheque: Cheque = db.query(Cheque)\
        .filter(Cheque.id == id)\
        .one_or_none()
    return cheque


def get_cheque_by_name(db: Session, name: str) -> Cheque:
    cheque: Cheque = db.query(Cheque)\
        .filter(Cheque.name == name)\
        .one_or_none()
    return cheque


def get_all_cheques(db: Session) -> List[Cheque]:
    cheques: List[Cheque] = db.query(Cheque).all()
    return cheques
