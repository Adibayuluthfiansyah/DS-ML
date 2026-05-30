import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

data_arsip = [
    "Laporan Keuangan Kuartal Pertama 2026",
    "Undangan Rapat Evaluasi Anggaran Tahunan",
    "Memo Internal Mengenai Cuti Bersama Tahunan",
    "Laporan Audit Keuangan Cabang Pontianak",
    "Surat Edaran Gubernur Mengenai Cuti Pegawai"
]

df = pd.DataFrame({"judul_dokumen": data_arsip})
print("--- DOKUMEN E-ARSIP ASLI ---")
print(df)
print("\n")

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['judul_dokumen'])


kamus_kata = vectorizer.get_feature_names_out()

print("--- KAMUS KATA YANG DIKENALI MESIN ---")
print(kamus_kata)
print(f"Total kata unik: {len(kamus_kata)} kata\n")

print("--- BENTUK MATRIKS TF-IDF (Dokumen 1) ---")
vektor_dokumen_1 = tfidf_matrix[0].toarray()
print(vektor_dokumen_1)