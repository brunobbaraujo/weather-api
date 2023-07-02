from helper import create_connection_string, read_config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

config = read_config("dbconfig.yml")

connection_string = create_connection_string(
    config["user"],
    config["password"],
    config["host"],
    config["port"],
    config["database"],
)
engine = create_engine(connection_string, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
