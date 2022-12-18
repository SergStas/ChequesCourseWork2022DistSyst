from sqlalchemy.orm import Session

from schemas.models import Cheque
from schemas.models_indexed import ChequeIndexed
from crud.cheques import get_cheque_by_id
from mappers.person import person_from_id
from mappers.position import position_from_id


def cheque_indexed_from_id(db: Session, id: int) -> ChequeIndexed:
    db_model = get_cheque_by_id(db=db, id=id)
    payer = person_from_id(db=db, id=db_model.payer)
    positions = [position_from_id(db=db, id=e.id) for e in db_model.positions]
    return ChequeIndexed(
        id=db_model.id,
        name=db_model.name,
        payer=payer,
        positions=positions,
    )


def cheque_from_id(db: Session, id: int) -> Cheque:
    db_model = get_cheque_by_id(db=db, id=id)
    payer = person_from_id(db=db, id=db_model.payer)
    positions = [position_from_id(db=db, id=e.id) for e in db_model.positions]
    return Cheque(
        name=db_model.name,
        payer=payer,
        positions=positions,
    )
