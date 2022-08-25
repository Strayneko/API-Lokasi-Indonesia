from sqlalchemy import Column, Integer, String
from app.models import Base


class Kelurahan(Base):
    __tablename__ = 'kelurahan'

    id           = Column('id', Integer, primary_key=True)
    id_kecamatan = Column('id_kecamatan', Integer)
    nama         = Column('nama', String)
