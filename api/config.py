from os import getenv
from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine
from dotenv import load_dotenv


load_dotenv()

DB_USER = getenv("PGUSER_DEV")
DB_PASSWORD = getenv("PGPASSWORD_DEV")
DB_NAME = getenv("PGDATABASE_DEV")
DB_HOST = getenv("PGHOST_DEV")

database_url = (
    f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    f"?sslmode=require&channel_binding=require"
)
engine = create_engine(database_url)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
