import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = {
    "waktu_di_web": [2, 3, 1, 15, 2, 4, 30, 2, 1, 3, 20, 1, 4, 25, 2],
    "jumlah_klik":  [5, 8, 2, 30, 6, 9, 60, 4, 2, 7, 45, 3, 10, 50, 5],
    "beli":         [0, 0, 0, 1,  0, 0, 1,  0, 0, 0, 1,  0, 0,  1,  0] 
}

df = pd.DataFrame(data)
X = df.drop(columns=['beli'])
y = df['beli']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)
prediksi = model.predict(X_test)
akurasi = accuracy_score(y_test, prediksi)
print(f"--- AKURASI BIASA: {akurasi * 100}% ---\n")


cm = confusion_matrix(y_test, prediksi)

print("--- CONFUSION MATRIX ---")
print(cm)
print("\n")


report = classification_report(y_test, prediksi)
print("--- CLASSIFICATION REPORT ---")
print(report)