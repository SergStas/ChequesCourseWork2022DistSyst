from sqlalchemy.orm import Session

from core.db.models import Person
from typing import List


def create_person(db: Session, name: str) -> Person:
    existing = get_person_by_name(db, name)
    if existing is not None:
        return existing
    person_db = Person(name=name)
    db.add(person_db)
    db.commit()
    return person_db


def get_person_by_name(db: Session, name: str) -> Person:
    person: Person = db.query(Person)\
        .filter(Person.name == name)\
        .one_or_none()
    return person


def get_person_by_id(db: Session, id: int) -> Person:
    person: Person = db.query(Person)\
        .filter(Person.id == id)\
        .one_or_none()
    return person


def get_all_persons(db: Session) -> List[Person]:
    persons: List[Person] = db.query(Person).all()
    return persons
