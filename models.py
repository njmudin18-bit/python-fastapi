from sqlalchemy import Column, Integer, String
from database import Base

class Item(Base):
    __tablename__ = "tbl_perusahaan"

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String(100))
    alamat = Column(String(100))