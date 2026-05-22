import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = {
    "transaction_id": ["T1", "T2", "T3", "T4"],
    "kategori": ["Elektronik", "Pakaian", "Elektronik", "Makanan"],
    "harga": [15000000, 250000, 5000000, 50000],
    "qty": [1, 3, 2, 5]
}

df = pd.DataFrame(data)

print("--- DATA ASLI ---")
print(df)
print("\n")


df = df.drop(columns=['transaction_id'])

df_encoded = pd.get_dummies(df, columns=['kategori'])


df_encoded = df_encoded.astype(int)

print("--- HASIL ONE HOT ENCODING ---")
print(df_encoded)
print("\n")


scaler = MinMaxScaler()
df_encoded[['harga', 'qty']] = scaler.fit_transform(
    df_encoded[['harga', 'qty']]
)

print("--- DATA SIAP MASUK MODEL MACHINE LEARNING ---")
print(df_encoded)