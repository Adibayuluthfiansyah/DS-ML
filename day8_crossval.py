import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score


np.random.seed(42)
waktu_di_web = np.random.randint(1, 40, 100)
jumlah_klik = waktu_di_web * np.random.uniform(0.5, 2.0, 100)
beli = np.where((waktu_di_web > 15) & (jumlah_klik > 20) & (np.random.rand(100) > 0.2), 1, 0)

df = pd.DataFrame({"waktu_di_web": waktu_di_web, "jumlah_klik": jumlah_klik, "beli": beli})

print("--- SAMPEL DATA TRANSAKSI ---")
print(df.head())
print(f"Total pembeli asli: {df['beli'].sum()} dari 100 pengunjung\n")


X = df.drop(columns=['beli'])
y = df['beli']
model_rf = RandomForestClassifier(random_state=42)


skor_lipatan = cross_val_score(model_rf, X, y, cv=5) 
print("--- HASIL UJIAN 5-FOLD CROSS VALIDATION ---")

print(f"Skor Akurasi per Lipatan: {skor_lipatan}")


rata_rata_skor = skor_lipatan.mean()
print(f"Rata-rata Skor Akurasi: {rata_rata_skor * 100:.2f}%")