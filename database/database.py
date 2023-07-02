from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database.helper import create_connection_string, read_config

config = read_config("database/dbconfig.yml")

connection_string = create_connection_string(
    config["user"],
    config["password"],
    config["host"],
    config["port"],
    config["database"],
)
engine = create_engine(connection_string, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
