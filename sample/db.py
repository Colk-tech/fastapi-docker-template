from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DB_ENGINE
from config import SYNC_POSTGRES_URL, SYNC_SQLITE_URL

if DB_ENGINE == "POSTGRESQL":
    SQLALCHEMY_DATABASE_URL = SYNC_POSTGRES_URL

    engine = create_engine(
        SYNC_POSTGRES_URL
    )

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

elif DB_ENGINE == "SQLITE":
    SQLALCHEMY_DATABASE_URL = SYNC_SQLITE_URL

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

else:
    raise RuntimeError("Runtime Error: no supported db system name")

Base = declarative_base()
