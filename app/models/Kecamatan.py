from sqlalchemy import Column, Integer, String
from app.models import Base


class Kecamatan(Base):
    __tablename__ = 'kecamatan'

    id           = Column('id', Integer,  primary_key=True)
    id_kabupaten = Column('id_kabupaten', Integer)
    nama         = Column('nama', String)
    