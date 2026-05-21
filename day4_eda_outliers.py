 # Untuk memisahkan data normal dari data ekstrem secara ilmiah, standar industri menggunakan rumus IQR (Interquartile Range)
 # IQR = Q3 - Q1 Batas atas data yang dianggap wajar didefinisikan sebagai
 # Batas Atas = Q3 + (1.5 * IQR)

import pandas as pd

data_penjualan = {
    "user_id": ["USR-01", "USR-02", "USR-03", "USR-04", "USR-05", "USR-06", "USR-07", "USR-08"],
    "total_belanja": [150000, 200000, 120000, 350000, 45000000, 180000, 220000, 300000]
}

df = pd.DataFrame(data_penjualan)
print("--- STATISTIK RINGKAS DATA ---")
print(df.describe())
print("\n")


# DETECT OUTLIERS
Q1 = df['total_belanja'].quantile(0.25)
Q3 = df['total_belanja'].quantile(0.75)
IQR = Q3 - Q1

# Batas atas untuk mendeteksi outliers
batas_atas = Q3 + (1.5 * IQR)
print(f"Nilai Q1    : Rp {Q1:,.2f}")
print(f"Nilai Q3    : Rp {Q3:,.2f}")
print(f"Nilai IQR   : Rp {IQR:,.2f}")
print(f"Batas Atas  : Rp {batas_atas:,.2f}")
print("\n")

# FILTER OUTLIERS
df_outliers = df[df['total_belanja'] > batas_atas]
print("--- DATA OUTLIERS ---")
print(df_outliers)





