from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.ext.asyncio import AsyncSession
from backend import models, schemas, crud
from backend.database import get_db, init_db
from typing import List

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://app.siteownr.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/")
async def read_root():
    return {"message": "Bank API Service"}

@app.get("/ping")
async def ping():
    return {"pong": True}

@app.post("/accounts/", response_model=schemas.Account)
async def create_account(account: schemas.AccountCreate, db: AsyncSession = Depends(get_db)):
    db_account = await crud.get_account_by_number(db, account.account_number)
    if db_account:
        raise HTTPException(status_code=400, detail="Account number already registered")
    new_account = models.Account(
        account_number=account.account_number,
        owner_name=account.owner_name,
        balance=account.initial_balance
    )
    return await crud.create_account(db, new_account)

@app.get("/accounts/", response_model=List[schemas.Account])
async def read_accounts(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    accounts = await crud.get_all_accounts(db, skip=skip, limit=limit)
    return accounts

@app.get("/accounts/{account_id}", response_model=schemas.Account)
async def read_account(account_id: int, db: AsyncSession = Depends(get_db)):
    db_account = await crud.get_account(db, account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account

@app.post("/accounts/{account_id}/deposit", response_model=schemas.Account)
async def deposit(account_id: int, transaction: schemas.Transaction, db: AsyncSession = Depends(get_db)):
    if transaction.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")
    account = await crud.update_account_balance(db, account_id, transaction.amount)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

@app.post("/accounts/{account_id}/withdraw", response_model=schemas.Account)
async def withdraw(account_id: int, transaction: schemas.Transaction, db: AsyncSession = Depends(get_db)):
    account = await crud.get_account(db, account_id)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    if transaction.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")
    if account.balance < transaction.amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")
    account = await crud.update_account_balance(db, account_id, -transaction.amount)
    return account