from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://postgres:123123@test_db:5432/db'

engine = create_engine(
    url=DATABASE_URL,
)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False
)
Base = declarative_base()
