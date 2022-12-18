from typing import List

import crud.positions as crud
import mappers.position as mapper
from deps import get_db
from fastapi import APIRouter
from fastapi import Depends
from schemas.models import Position
from schemas.models_indexed import PositionIndexed

router = APIRouter(prefix="/positions")


@router.post('/', response_model=PositionIndexed)
def create_position(position: Position, db=Depends(get_db)):
    result = crud.create_position(db=db, name=position.name, cost=position.cost, owner_name=position.owner.name)
    return mapper.position_indexed_from_id(db=db, id=result.id)


@router.get('/', response_model=List[PositionIndexed])
def get_all(db=Depends(get_db)):
    result = crud.get_all_positions(db=db)
    return [mapper.position_indexed_from_id(db=db, id=e.id) for e in result]
