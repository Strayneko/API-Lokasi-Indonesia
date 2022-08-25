from sqlalchemy import Column, Integer, String
from app.models import Base


class Kabupaten(Base):
    __tablename__ = 'kabupaten'

    id          = Column('id', Integer, primary_key=True)
    id_provinsi = Column('id_provinsi', Integer)
    nama        = Column('nama', String)
