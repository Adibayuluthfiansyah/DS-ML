# It's easier to ask for forgiveness than permission EAFP

import json
keranjang_user = [
    {"nama": "Mechanical Keyboard", "harga": 850000},
    {"nama": "Monitor 4K", "harga": 5000000}
]

def simpan_keranjang(data, nama_file):
    try:
        with open(nama_file, "w") as f:
            json.dump(data, f)
        print(f"Berhasil menyimpan data ke {nama_file}")
    except Exception as e:
        print(f"Gagal menyimpan file. Error: {e}")

def baca_keranjang(nama_file):
    try:
        with open(nama_file, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error saat membaca file: {e}")
        return []
    except FileNotFoundError:
        print(f"Peringatan: File {nama_file} tidak ditemukan. Membuat keranjang baru.")
        return []

simpan_keranjang(keranjang_user, "keranjang_db.json")
data_tersimpan = baca_keranjang("keranjang_db.json")
print(f"Data yang di-load: {data_tersimpan}")
data_kosong = baca_keranjang("file_gaib.json")
print(f"Data dari file gaib: {data_kosong}")