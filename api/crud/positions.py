from typing import List

from sqlalchemy.orm import Session

from core.db.models import Position
from crud.persons import get_person_by_name, create_person


def create_position(db: Session, name: str, cost: float, owner_name: str) -> Position:
    owner_db = get_person_by_name(db=db, name=owner_name)
    if owner_db is None:
        owner_db = create_person(db=db, name=owner_name)
    position_db = Position(name=name, cost=cost, owner_id=owner_db.id)
    db.add(position_db)
    db.commit()
    return position_db


def get_position_by_id(db: Session, id: int) -> Position:
    position: Position = db.query(Position)\
        .filter(Position.id == id)\
        .one_or_none()
    return position


def get_all_positions(db: Session) -> List[Position]:
    positions: List[Position] = db.query(Position).all()
    return positions
