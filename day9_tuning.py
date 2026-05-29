import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV


np.random.seed(42)
waktu_di_web = np.random.randint(1, 40, 100)
jumlah_klik = waktu_di_web * np.random.uniform(0.5, 2.0, 100)
beli = np.where((waktu_di_web > 15) & (jumlah_klik > 20) & (np.random.rand(100) > 0.2), 1, 0)
df = pd.DataFrame({"waktu_di_web": waktu_di_web, "jumlah_klik": jumlah_klik, "beli": beli})

X = df.drop(columns=['beli'])
y = df['beli']


model_rf = RandomForestClassifier(random_state=42)
param_grid = {
    'n_estimators': [10, 50, 100],
    'max_depth': [3, 5, None]
}

print("Memulai proses Grid Search (Mencoba 9 kombinasi x 5 Fold = 45 kali training)...")
grid_search = GridSearchCV(model_rf, param_grid, cv=5) 
grid_search.fit(X, y)


print("--- HASIL OPTIMASI MESIN ---")
print(f"Konfigurasi Terbaik : {grid_search.best_params_}")
print(f"Akurasi Terbaik     : {grid_search.best_score_ * 100:.2f}%")