from typing import List

import crud.results as crud
import mappers.result as mapper
from deps import get_db
from fastapi import APIRouter
from fastapi import Depends
from schemas.models import CalculationResult
from schemas.models_indexed import CalculationResultIndexed

router = APIRouter(prefix="/results")


@router.post('/', response_model=CalculationResultIndexed)
def create_result(input_result: CalculationResult, db=Depends(get_db)):
    result = crud.create_result(
        db=db,
        cheque_id=input_result.cheque_id,
        transactions=input_result.transactions,
    )
    return mapper.result_indexed_from_id(db=db, id=result.id)


@router.get('/', response_model=List[CalculationResultIndexed])
def get_all(db=Depends(get_db)):
    result = crud.get_all_results(db=db)
    return [mapper.result_indexed_from_id(db=db, id=e.id) for e in result]
