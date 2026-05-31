import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

df_train = pd.DataFrame({
    "dokumen": [
        "Laporan laba rugi dan neraca",
        "Faktur pembayaran pajak",
        "Surat peringatan kedisiplinan absen",
        "Formulir pengajuan cuti karyawan",
        "Jadwal perbaikan lift gedung utama",
        "Pengadaan inventaris meja kursi kantor"
    ],
    "kategori": ["Keuangan", "Keuangan", "HRD", "HRD", "Operasional", "Operasional"]
})


dokumen_baru = [
    "Tagihan bulanan langganan server AWS",
    "Aturan jam kerja karyawan selama bulan ramadhan"
]


model_ai = make_pipeline(TfidfVectorizer(), MultinomialNB())
model_ai.fit(df_train['dokumen'], df_train['kategori']) 
prediksi_kategori = model_ai.predict(dokumen_baru)
print("--- HASIL KLASIFIKASI OTOMATIS E-ARSIP ---")
for teks, kategori in zip(dokumen_baru, prediksi_kategori):
    print(f"Dokumen : '{teks}'\nPrediksi Kategori: {kategori}\n")