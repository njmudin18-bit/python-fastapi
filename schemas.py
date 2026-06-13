from pydantic import BaseModel
from typing import Any, List

# 1. Definisikan skema untuk data Item itu sendiri
class ItemBase(BaseModel):
    id: int
    nama: str
    alamat: str

    class Config:
        # Ini kunci penting agar Pydantic bisa membaca objek SQLAlchemy
        from_attributes = True 

# 2. Gunakan skema di atas untuk membungkus respon
class ResponseModel(BaseModel):
    status: str
    status_code: int
    message: str
    data: Any # Any bisa diganti List[ItemBase] agar lebih spesifik