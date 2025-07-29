from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import text

from backend.config import settings


engine = create_async_engine(settings.DATABASE_URL, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()

async def init_db():
    async with engine.begin() as conn:
        await conn.execute(text("CREATE SCHEMA IF NOT EXISTS bankapp"))
        await conn.run_sync(Base.metadata.create_all)

async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session