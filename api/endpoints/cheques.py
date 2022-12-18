from typing import List
from fastapi import APIRouter
from fastapi import Depends
from deps import get_db
from schemas.models import Cheque, Person, Position
from schemas.models_indexed import ChequeIndexed
import crud.cheques as crud
import mappers.cheque as mapper

router = APIRouter(prefix="/cheques")


@router.post('/', response_model=ChequeIndexed)
def create_cheque(cheque: Cheque, db=Depends(get_db)):
    result = crud.create_cheque(
        db=db,
        name=cheque.name,
        payer_name=cheque.payer.name,
        positions=cheque.positions,
    )
    return mapper.cheque_indexed_from_id(db=db, id=result.id)


@router.get('/', response_model=List[ChequeIndexed])
def get_all(db=Depends(get_db)):
    result = crud.get_all_cheques(db=db)
    return [mapper.cheque_indexed_from_id(db=db, id=e.id) for e in result]
