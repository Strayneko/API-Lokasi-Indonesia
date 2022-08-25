from sqlalchemy import Column, Integer, String
from app.models import Base


class Provinsi(Base):
    __tablename__ = 'provinsi'

    id = Column('id', Integer, primary_key=True)
    nama = Column('nama', String)
