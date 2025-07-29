from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend import models
from decimal import Decimal


async def create_account(db: AsyncSession, account: models.Account):
    db.add(account)
    await db.commit()
    await db.refresh(account)
    return account

async def get_account(db: AsyncSession, account_id: int):
    result = await db.execute(select(models.Account).filter(models.Account.id == account_id))
    return result.scalars().first()

async def get_account_by_number(db: AsyncSession, account_number: str):
    result = await db.execute(select(models.Account).filter(models.Account.account_number == account_number))
    return result.scalars().first()

async def update_account_balance(db: AsyncSession, account_id: int, amount: float):
    account = await get_account(db, account_id)
    if account:
        account.balance += Decimal(amount)
        await db.commit()
        await db.refresh(account)
    return account

async def get_all_accounts(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(models.Account).offset(skip).limit(limit))
    return result.scalars().all()