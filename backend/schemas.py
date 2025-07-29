from pydantic import BaseModel
from typing import Optional

class AccountBase(BaseModel):
    account_number: str
    owner_name: str

class AccountCreate(AccountBase):
    initial_balance: float = 0.0

class Account(AccountBase):
    id: int
    balance: float

    class Config:
        from_attributes = True

class Transaction(BaseModel):
    amount: float
    description: Optional[str] = None