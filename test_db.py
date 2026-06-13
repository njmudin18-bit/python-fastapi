from sqlalchemy import create_engine, text

# Ganti 'nama_database_anda' dengan nama database yang sudah ada di phpMyAdmin
URL_DATABASE = "mysql+pymysql://root:@localhost:3309/omas_ticketing"

try:
    # 1. Buat koneksi
    engine = create_engine(URL_DATABASE)
    
    # 2. Coba hubungkan dan jalankan perintah simpel
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 'Koneksi Berhasil!'"))
        for row in result:
            print(f"--- {row[0]} ---")
            
    print("Selamat! FastAPI sudah bisa ngobrol dengan MySQL.")

except Exception as e:
    print("Waduh, koneksi gagal!")
    print(f"Errornya adalah: {e}")