import pandas as pd
import numpy as np


data = {
    "transaction_id": ["TRX-01", "TRX-02", "TRX-03", "TRX-04", "TRX-05", "TRX-06"],
    "kategori": ["Elektronik", "Pakaian", "Elektronik", "Makanan", "Pakaian", "Elektronik"],
    "harga": [15000000, 250000, 5000000, 50000, 150000, 3000000],
    "qty": [1, np.nan, 2, 5, np.nan, 1] 
}


df = pd.DataFrame(data)

print("--- DATA TRANSAKSI MENTAH ---")
print(df)
print("\n")

# ==========================================
# TUGAS DATA WRANGLING
# ==========================================

# TUGAS 1: DATA CLEANING
# Sistem POS (Point of Sales) kadang gagal mencatat qty. 
# Asumsi bisnis: Jika qty kosong (NaN), berarti pelanggan membeli 1 barang.
# Isi/replace semua nilai NaN di kolom 'qty' dengan angka 1.
df['qty'] = df['qty'].fillna(1) # <--- UBAH BARIS INI (Gunakan method .fillna())

# TUGAS 2: FEATURE ENGINEERING (Vectorization)
# Buat kolom baru bernama 'revenue' yang merupakan hasil kali kolom 'harga' dan 'qty'
# Lakukan tanpa for-loop!
df['revenue'] = df['harga'] * df['qty'] # <--- UBAH BARIS INI

# TUGAS 3: AGGREGATION (Group By)
# Bos E-Commerce meminta laporan: "Berapa total revenue untuk masing-masing kategori?"
# Kelompokkan data berdasarkan 'kategori', lalu jumlahkan (sum) 'revenue'-nya.
laporan_revenue = df.groupby('kategori')['revenue'].sum() # <--- UBAH BARIS INI (Gunakan .groupby() dan .sum())

print("--- DATA TRANSAKSI BERSIH ---")
print(df)
print("\n")

print("--- LAPORAN REVENUE PER KATEGORI ---")
print(laporan_revenue)