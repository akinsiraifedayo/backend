from sqlalchemy import Column, Integer, String, Numeric
from backend.database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String, unique=True, index=True)
    owner_name = Column(String)
    balance = Column(Numeric(10, 2), default=0.0)