import requests
import json # Library tambahan untuk mengolah JSON

# 1. URL dan Headers tetap sama sesuai gambar inspeksi Bapak
url = 'https://omas-mfg.com/api/power_cord_series_list/power-cord-series'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Accept': 'application/json'
}

try:
    # 2. Kirim permintaan GET ke API
    response = requests.get(url, headers=headers)
    
    # 3. Pastikan status code 200 (Berhasil)
    if response.status_code == 200:
        json_data = response.json()
        
        # 4. Ambil bagian 'data' saja
        daftar_produk = json_data.get('data', [])
        
        # 5. Simpan ke file .json lokal
        nama_file = 'data_produk_omas.json'
        with open(nama_file, 'w', encoding='utf-8') as f:
            # indent=4 agar file JSON rapi dan mudah dibaca
            json.dump(daftar_produk, f, ensure_ascii=False, indent=4)
        
        print(f"Berhasil! {len(daftar_produk)} data produk telah dijadikan file: {nama_file}")
            
    else:
        print(f"Gagal mengambil data. Status Code: {response.status_code}")

except Exception as e:
    print(f"Terjadi kesalahan: {e}")