from sqlalchemy import create_engine

from config import DB_ENGINE
from config import SYNC_POSTGRES_URL, SYNC_SQLITE_URL

# Import Declarative Base Here

if DB_ENGINE == "POSTGRESQL":
    SQLALCHEMY_DATABASE_URL = SYNC_POSTGRES_URL

elif DB_ENGINE == "SQLITE":
    SQLALCHEMY_DATABASE_URL = SYNC_SQLITE_URL

else:
    raise RuntimeError("Runtime Error: no supported db system name")

DB_URL = SQLALCHEMY_DATABASE_URL
engine = create_engine(DB_URL, echo=True)


def reset_database():
    # Call
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)
    # For each bases
    pass


if __name__ == "__main__":
    reset_database()
