import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data_arsip = [
    "Laporan Keuangan Kuartal Pertama 2026",
    "Undangan Rapat Evaluasi Anggaran Tahunan",
    "Memo Internal Mengenai Cuti Bersama Tahunan",
    "Laporan Audit Keuangan Cabang Pontianak",
    "Surat Edaran Gubernur Mengenai Cuti Pegawai"
]
df = pd.DataFrame({"judul_dokumen": data_arsip})

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['judul_dokumen'])


query_pencarian = ["audit keuangan tahunan"]
vektor_query = vectorizer.transform(query_pencarian) 
skor_kemiripan = cosine_similarity(vektor_query, tfidf_matrix)

print("--- HASIL PENCARIAN E-ARSIP ---")
print(f"Query: '{query_pencarian[0]}'\n")
df['skor_relevansi'] = skor_kemiripan[0]
df_sorted = df.sort_values(by='skor_relevansi', ascending=False)

print(df_sorted[['skor_relevansi', 'judul_dokumen']])