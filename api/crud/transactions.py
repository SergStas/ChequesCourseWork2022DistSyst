from typing import List

from sqlalchemy.orm import Session

from core.db.models import Transaction
from crud.persons import get_person_by_name, create_person


def create_transaction(db: Session, sender_name: str, sum: float, receiver_name: str) -> Transaction:
    sender_db = get_person_by_name(db=db, name=sender_name)
    if sender_db is None:
        sender_db = create_person(db=db, name=sender_name)
    receiver_db = get_person_by_name(db=db, name=receiver_name)
    if receiver_db is None:
        receiver_db = create_person(db=db, name=receiver_name)
    transaction_db = Transaction(sum=sum, sender_id=sender_db.id, receiver_id=receiver_db.id)
    db.add(transaction_db)
    db.commit()
    return transaction_db


def get_transaction_by_id(db: Session, id: int) -> Transaction:
    transaction: Transaction = db.query(Transaction)\
        .filter(Transaction.id == id)\
        .one_or_none()
    return transaction


def get_all_transactions(db: Session) -> List[Transaction]:
    transactions: List[Transaction] = db.query(Transaction).all()
    return transactions
