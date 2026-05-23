import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


data = {
    "waktu_di_web": [5, 15, 2, 25, 10, 3, 30, 12, 1, 20],
    "jumlah_klik": [10, 35, 5, 50, 20, 8, 60, 25, 2, 40],
    "item_di_keranjang": [0, 2, 0, 3, 1, 0, 5, 1, 0, 2],
    "beli": [0, 1, 0, 1, 0, 0, 1, 1, 0, 1] 
}

df = pd.DataFrame(data)
print("--- DATA PERILAKU PENGGUNA ---")
print(df.head())
print("\n")

# PIPELINE
X = df.drop(columns=['beli'])
y = df['beli']

# --- LANGKAH 2: TRAIN-TEST SPLIT ---
# Membelah 80% data Train, 20% data Test
# random_state=42 digunakan agar pemisahan data selalu sama setiap kali script dijalankan (standar reproduksibilitas eksperimen)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- LANGKAH 3: TRAINING MODEL (Otak AI Belajar) ---
model = LogisticRegression()

# TUGAS 1: Latih model menggunakan data training (X_train dan y_train)
# Gunakan method .fit()
# TULIS KODEMU DI BAWAH INI:
model.fit(X_train, y_train)

# --- LANGKAH 4: PREDIKSI & EVALUASI ---
# TUGAS 2: Suruh model memprediksi data ujian (X_test) menggunakan method .predict()
# Simpan hasilnya di variabel bernama 'prediksi'
# TULIS KODEMU DI BAWAH INI:
prediksi = model.predict(X_test)

# Kita kalkulasi akurasinya dengan membandingkan jawaban asli ujian (y_test) dengan tebakan model (prediksi)
akurasi = accuracy_score(y_test, prediksi)

print("--- HASIL UJIAN MODEL ---")
print(f"Jawaban Asli (y_test) : {y_test.values}")
print(f"Tebakan Model         : {prediksi}")
print(f"Akurasi Model         : {akurasi * 100}%")