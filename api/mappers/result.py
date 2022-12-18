from sqlalchemy.orm import Session

from schemas.models import CalculationResult
from schemas.models_indexed import CalculationResultIndexed
from crud.results import get_result_by_id
from mappers.transaction import transaction_from_id


def result_indexed_from_id(db: Session, id: int) -> CalculationResultIndexed:
    db_model = get_result_by_id(db=db, id=id)
    tr = [transaction_from_id(db=db, id=t.id) for t in db_model.transactions]
    return CalculationResultIndexed(id=db_model.id, cheque_id=db_model.cheque_id, transactions=tr)


def result_from_id(db: Session, id: int) -> CalculationResult:
    db_model = get_result_by_id(db=db, id=id)
    tr = [transaction_from_id(db=db, id=t.id) for t in db_model.transactions]
    return CalculationResult(cheque_id=db_model.cheque_id, transactions=tr)
