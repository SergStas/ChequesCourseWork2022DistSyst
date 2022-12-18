from sqlalchemy.orm import Session

from schemas.models import Person
from schemas.models_indexed import PersonIndexed
from crud.persons import get_person_by_id


def person_indexed_from_id(db: Session, id: int) -> PersonIndexed:
    db_model = get_person_by_id(db=db, id=id)
    return PersonIndexed(id=db_model.id, name=db_model.name)


def person_from_id(db: Session, id: int) -> Person:
    db_model = get_person_by_id(db=db, id=id)
    return Person(name=db_model.name)
