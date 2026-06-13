import os
import secrets
from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from typing import List
from dotenv import load_dotenv

# Import file lokal kita
import models
import schemas
from database import engine, get_db

# Load variabel dari file .env
load_dotenv()
API_USER = os.getenv("API_USER")
API_PASS = os.getenv("API_PASS")

# Inisialisasi Security
security = HTTPBasic()

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    is_username_correct = secrets.compare_digest(credentials.username, API_USER)
    is_password_correct = secrets.compare_digest(credentials.password, API_PASS)
    
    if not (is_username_correct and is_password_correct):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Kredensial Aplikasi Salah",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

# Membuat tabel di database
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Latihan FastAPI & MySQL")

# --- ENDPOINT YANG SUDAH DIMODIFIKASI ---

@app.get("/", response_model=schemas.ResponseModel)
def root(username: str = Depends(get_current_user)):
    return {
        "status": "success",
        "status_code": 200,
        "message": f"Halo {username}, API Berhasil Terhubung",
        "data": None
    }

@app.get("/items", response_model=schemas.ResponseModel)
def lihat_semua_barang(
    db: Session = Depends(get_db), 
    username: str = Depends(get_current_user) # Penjaga pintu masuk
):
    try:
        items = db.query(models.Item).all()
        return {
            "status": "success",
            "status_code": 200,
            "message": f"Data berhasil diambil oleh {username}",
            "data": jsonable_encoder(items)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))