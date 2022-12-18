from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Position(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    cost = Column(Float)
    owner_id = Column(Integer, ForeignKey("persons.id"))
    cheque_id = Column(Integer, ForeignKey("cheques.id"))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Cheque(Base):
    __tablename__ = "cheques"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    positions = relationship("Position")
    payer_id = Column(Integer, ForeignKey("persons.id"))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    sum = Column(Float)
    sender_id = Column(Integer, ForeignKey("persons.id"))
    receiver_id = Column(Integer, ForeignKey("persons.id"))
    result_id = Column(Integer, ForeignKey("results.id"))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class CalculationResult(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True)
    transactions = relationship("Transaction")
    cheque_id = Column(Integer, ForeignKey("cheques.id"))
