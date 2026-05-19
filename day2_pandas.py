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
# DATA WRANGLING
# ==========================================

# DATA CLEANING
df['qty'] = df['qty'].fillna(1) # <--- UBAH BARIS INI (Gunakan method .fillna())

# FEATURE ENGINEERING (Vectorization)
df['revenue'] = df['harga'] * df['qty'] 

# AGGREGATION (Group By)
# Bos E-Commerce meminta laporan: "Berapa total revenue untuk masing-masing kategori?"

laporan_revenue = df.groupby('kategori')['revenue'].sum() 

print("--- DATA TRANSAKSI BERSIH ---")
print(df)
print("\n")

print("--- LAPORAN REVENUE PER KATEGORI ---")
print(laporan_revenue)