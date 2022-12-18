from sqlalchemy.orm import Session

from schemas.models import Position
from schemas.models_indexed import PositionIndexed
from crud.positions import get_position_by_id
from mappers.person import person_from_id


def position_indexed_from_id(db: Session, id: int) -> PositionIndexed:
    db_model = get_position_by_id(db=db, id=id)
    owner = person_from_id(db=db, id=db_model.owner_id)
    return PositionIndexed(id=db_model.id, name=db_model.name, cost=db_model.cost, owner=owner)


def position_from_id(db: Session, id: int) -> Position:
    db_model = get_position_by_id(db=db, id=id)
    owner = person_from_id(db=db, id=db_model.owner_id)
    return Position(name=db_model.name, cost=db_model.cost, owner=owner)
