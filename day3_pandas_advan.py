import pandas as pd


df_produk = pd.DataFrame({
    "product_id": ["P-101", "P-102", "P-103", "P-104"],
    "nama_produk": ["Laptop Pro X", "Mouse Wireless", "Keyboard Mekanik", "Monitor 4K"],
    "kategori": ["Elektronik", "Aksesoris", "Aksesoris", "Elektronik"],
    "harga_satuan": [15000000, 350000, 850000, 5000000]
})


df_transaksi = pd.DataFrame({
    "transaction_id": ["TX-901", "TX-902", "TX-903", "TX-904", "TX-905"],
    "product_id": ["P-101", "P-103", "P-101", "P-102", "P-104"],
    "qty": [1, 2, 1, 5, 2]
})

print("--- DATA MASTER PRODUK ---")
print(df_produk)
print("\n--- LOG TRANSAKSI MENTAH ---")
print(df_transaksi)
print("\n")

# =============================================================
# TUGAS ADVANCED DATA ANALYTICS
# =============================================================

# TUGAS 1: RELATIONAL MERGE (SQL JOIN)
# Gabungkan df_transaksi dengan df_produk berdasarkan kolom 'product_id'.
# Gunakan metode inner join agar hanya data yang berpasangan yang diambil.
df_gabung = pd.merge(df_transaksi, df_produk, on='product_id', how='inner') # <--- UBAH BARIS INI (Gunakan pd.merge())

# TUGAS 2: FEATURE ENGINEERING
# Buat kolom baru bernama 'total_bayar' hasil perkalian 'qty' dan 'harga_satuan'
df_gabung['total_bayar'] = df_gabung['qty'] * df_gabung['harga_satuan'] # <--- UBAH BARIS INI

# TUGAS 3: MULTI-AGGREGATION DASBOR
# Buat rangkuman analitik per KATEGORI yang menampilkan dua hal sekaligus:
# A. Total Pendapatan (sum dari 'total_bayar')
# B. Rata-rata Pembelian (mean dari 'total_bayar')
# Petunjuk: Gunakan .groupby('kategori')['total_bayar'].agg(['sum', 'mean'])
dasbor_analitik = df_gabung.groupby('kategori')['total_bayar'].agg(['sum', 'mean']) # <--- UBAH BARIS INI

print("--- HASIL PENGGABUNGAN DATA ---")
print(df_gabung[['transaction_id', 'nama_produk', 'kategori', 'qty', 'total_bayar']])
print("\n")

print("--- DASBOR ANALITIK BISNIS ---")
print(dasbor_analitik.round())