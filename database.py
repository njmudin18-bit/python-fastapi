from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Format: mysql+pymysql://username:password@host:port/nama_db
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost:3309/omas_ticketing"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Fungsi untuk mendapatkan sesi database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()