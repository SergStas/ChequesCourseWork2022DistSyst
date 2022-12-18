from typing import List
from fastapi import APIRouter
from fastapi import Depends
from deps import get_db
from schemas.models import Person
from schemas.models_indexed import PersonIndexed
import crud.persons as crud
import mappers.person as mapper

router = APIRouter(prefix="/persons")


@router.post('/', response_model=PersonIndexed)
def create_person(person: Person, db=Depends(get_db)):
    result = crud.create_person(db=db, name=person.name)
    return mapper.person_indexed_from_id(db=db, id=result.id)


@router.get('/', response_model=List[PersonIndexed])
def get_all(db=Depends(get_db)):
    result = crud.get_all_persons(db=db)
    return [mapper.person_indexed_from_id(db=db, id=e.id) for e in result]
