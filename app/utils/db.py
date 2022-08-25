import sqlalchemy as sa
from app.config import config

db_engine = sa.create_engine(
    config.DB,
    pool_pre_ping=config.DB_POOL_PRE_PING,
    pool_recycle=config.DB_POOL_RECYCLE,
    echo=config.DB_ECHO
)
