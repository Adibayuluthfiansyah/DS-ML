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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LogisticRegression()
model.fit(X_train, y_train)
prediksi = model.predict(X_test)
akurasi = accuracy_score(y_test, prediksi)

print("--- HASIL UJIAN MODEL ---")
print(f"Jawaban Asli (y_test) : {y_test.values}")
print(f"Tebakan Model         : {prediksi}")
print(f"Akurasi Model         : {akurasi * 100}%")