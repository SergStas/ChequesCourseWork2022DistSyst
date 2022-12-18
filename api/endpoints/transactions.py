from typing import List

import crud.transactions as crud
import mappers.transaction as mapper
from deps import get_db
from fastapi import APIRouter
from fastapi import Depends
from schemas.models import Transaction
from schemas.models_indexed import TransactionIndexed

router = APIRouter(prefix="/transactions")


@router.post('/', response_model=TransactionIndexed)
def create_transaction(transaction: Transaction, db=Depends(get_db)):
    result = crud.create_transaction(
        db=db,
        sum=transaction.sum,
        sender_name=transaction.sender.name,
        receiver_name=transaction.receiver.name,
    )
    return mapper.transaction_indexed_from_id(db=db, id=result.id)


@router.get('/', response_model=List[TransactionIndexed])
def get_all(db=Depends(get_db)):
    result = crud.get_all_transactions(db=db)
    return [mapper.transaction_indexed_from_id(db=db, id=e.id) for e in result]
