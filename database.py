from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB=URL ="sqlite+aiosqlite:///fastapi-app.db"
engine = create_async_engine(DB_URL, echo=True)

Base = declarative_base()

db_session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)

async def get_db():
    async with db_session() as session:
        yield session
