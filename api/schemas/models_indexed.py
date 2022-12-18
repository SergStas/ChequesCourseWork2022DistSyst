from schemas.models import *


class PersonIndexed(Person):
    id: int


class PositionIndexed(Position):
    id: int


class ChequeIndexed(Cheque):
    id: int


class TransactionIndexed(Transaction):
    id: int


class CalculationResultIndexed(CalculationResult):
    id: int
