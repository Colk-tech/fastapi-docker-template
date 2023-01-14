from typing import Type, Optional, Literal, get_args
from os import getenv, environ

# Constants
APIChannel: Type = Literal["Develop", "Staging", "Production"]
SupportedDBS: Type = Literal["POSTGRESQL", "SQLITE"]

API_SERVICE_NAME: str = "payment-service"
API_VERSION: str = "0.0.0"
API_CHANNEL: APIChannel = "Develop"

JWT_AUDIENCE: str = API_SERVICE_NAME

# 300 sec ( 5 min )
DEFAULT_FINGERPRINT_TOKEN_LIFETIME_SEC: int = 300
DEFAULT_ONETIME_TOKEN_LIFETIME_SEC: int = 60

# Optional
IS_DEBUG: Optional[bool] = None if getenv("FP_PAY_IS_DEBUG") is None else bool("FP_PAY_IS_DEBUG")

# Required
MY_HOST: str = environ["FP_PAY_MY_HOST"]
MY_WORKER_NAME: str = environ["FP_PAY_MY_WORKER_NAME"]

DB_ENGINE: SupportedDBS = environ["FP_PAY_DB_ENGINE"]

if DB_ENGINE not in get_args(SupportedDBS):
    raise RuntimeError(
        f"Runtime Error: unexpected DB system name. "
        f"supported systems are: {get_args(SupportedDBS)}"
    )

if DB_ENGINE == "POSTGRESQL":
    POSTGRES_USER_NAME: str = environ["FP_PAY_POSTGRES_USER_NAME"]
    POSTGRES_PASSWORD: str = environ["FP_PAY_POSTGRES_PASSWORD"]
    POSTGRES_DB_NAME: str = environ["FP_PAY_POSTGRES_DB_NAME"]
    POSTGRES_HOST: str = environ["FP_PAY_POSTGRES_HOST"]
    POSTGRES_PORT: int = int(environ["FP_PAY_POSTGRES_PORT"])

if DB_ENGINE == "SQLITE":
    SQLITE_PATH: str = environ["FP_PAY_SQLITE_PATH"]

FIREBASE_KEY_PATH: str = environ["FP_PAY_FIREBASE_KEY_PATH"]

JWT_SECRET: str = environ["FP_PAY_JWT_SECRET"]

# Evaluated
ASYNC_POSTGRES_URL: Optional[str] = None
SYNC_POSTGRES_URL: Optional[str] = None
SYNC_SQLITE_URL: Optional[str] = None

if DB_ENGINE == "POSTGRESQL":
    ASYNC_POSTGRES_URL: str = f"postgresql+asyncpg://" \
                              f"{POSTGRES_USER_NAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB_NAME}"
    SYNC_POSTGRES_URL: str = f"postgresql://" \
                             f"{POSTGRES_USER_NAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB_NAME}"

if DB_ENGINE == "SQLITE":
    SYNC_SQLITE_URL: str = "sqlite:///" \
                           f"{SQLITE_PATH}"

JWT_ALGORITHM: str = "HS256"
JWT_ISSUER: str = MY_WORKER_NAME

if IS_DEBUG:
    # 3600 sec ( 60 min )
    DEFAULT_FINGERPRINT_TOKEN_LIFETIME_SEC = 3600
    DEFAULT_ONETIME_TOKEN_LIFETIME_SEC = 3600
