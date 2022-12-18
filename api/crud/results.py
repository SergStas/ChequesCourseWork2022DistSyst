from typing import List

from sqlalchemy.orm import Session

from core.db.models import CalculationResult
from crud.transactions import create_transaction


def create_result(db: Session, cheque_id: int, transactions) -> CalculationResult:
    tr_db = [
        create_transaction(db=db, sum=t.sum, sender_name=t.sender.name, receiver_name=t.receiver.name)
        for t in transactions
    ]
    result_db = CalculationResult(cheque_id=cheque_id, transactions=tr_db)
    db.add(result_db)
    db.commit()
    return result_db


def get_result_by_id(db: Session, id: int) -> CalculationResult:
    result: CalculationResult = db.query(CalculationResult)\
        .filter(CalculationResult.id == id)\
        .one_or_none()
    return result


def get_all_results(db: Session) -> List[CalculationResult]:
    results: List[CalculationResult] = db.query(CalculationResult).all()
    return results
