from sqlalchemy.orm import Session

from schemas.models import Transaction
from schemas.models_indexed import TransactionIndexed
from crud.transactions import get_transaction_by_id
from mappers.person import person_from_id


def transaction_indexed_from_id(db: Session, id: int) -> TransactionIndexed:
    db_model = get_transaction_by_id(db=db, id=id)
    sender = person_from_id(db=db, id=db_model.sender_id)
    receiver = person_from_id(db=db, id=db_model.receiver_id)
    return TransactionIndexed(id=db_model.id, sum=db_model.sum, sender=sender, receiver=receiver)


def transaction_from_id(db: Session, id: int) -> Transaction:
    db_model = get_transaction_by_id(db=db, id=id)
    sender = person_from_id(db=db, id=db_model.sender_id)
    receiver = person_from_id(db=db, id=db_model.receiver_id)
    return Transaction(sum=db_model.sum, sender=sender, receiver=receiver)
