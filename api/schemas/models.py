from typing import List

from pydantic import BaseModel


class Person(BaseModel):
    name: str


class Position(BaseModel):
    name: str
    cost: float
    owner: Person


class Cheque(BaseModel):
    positions: List[Position]
    name: str
    payer: Person


class Transaction(BaseModel):
    sender: Person
    receiver: Person
    sum: float


class CalculationResult(BaseModel):
    cheque_id: int
    transactions: List[Transaction]
