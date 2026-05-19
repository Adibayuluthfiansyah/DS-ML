import time
import numpy as np
import random


UKURAN_DATA = 100_000_0

print(f"Menyiapkan data sebanyak {UKURAN_DATA}...")
list_a = [random.random() for _ in range(UKURAN_DATA)]
list_b = [random.random() for _ in range(UKURAN_DATA)]

arr_a = np.array(list_a)
arr_b = np.array(list_b)

mulai_python = time.perf_counter()

hasil_python = [a * b for a, b in zip(list_a, list_b)]

selesai_python = time.perf_counter()

waktu_python = selesai_python - mulai_python

print(f"Waktu yang dibutuhkan untuk operasi dengan Python murni: {waktu_python:.5f} detik")

print("Validasi: hasil identik ")

mulai_numpy = time.perf_counter()

hasil_numpy = arr_a * arr_b

selesai_numpy = time.perf_counter()

waktu_numpy = selesai_numpy - mulai_numpy  

print(f"Waktu yang dibutuhkan untuk operasi dengan NumPy: {waktu_numpy:.5f} detik")
assert np.allclose(hasil_python, hasil_numpy), "Hasil tidak sama!"
print("Validasi: hasil identik ")


print(f"Percepatan dengan NumPy: {waktu_python / waktu_numpy:.2f}x")
