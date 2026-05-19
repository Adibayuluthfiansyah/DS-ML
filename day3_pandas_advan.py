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
# DATA ANALYTICS
# =============================================================


df_gabung = pd.merge(df_transaksi, df_produk, on='product_id', how='inner')


df_gabung['total_bayar'] = df_gabung['qty'] * df_gabung['harga_satuan'] 

# MULTI-AGGREGATION DASBOR
# Buat rangkuman analitik per KATEGORI yang menampilkan dua hal sekaligus:
dasbor_analitik = df_gabung.groupby('kategori')['total_bayar'].agg(['sum', 'mean']) # <--- UBAH BARIS INI

print("--- HASIL PENGGABUNGAN DATA ---")
print(df_gabung[['transaction_id', 'nama_produk', 'kategori', 'qty', 'total_bayar']])
print("\n")

print("--- DASBOR ANALITIK BISNIS ---")
print(dasbor_analitik.round())