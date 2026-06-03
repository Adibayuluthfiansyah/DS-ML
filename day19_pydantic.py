from pydantic import BaseModel, ValidationError
from typing import List, Optional, ClassVar

class PayloadDokumen(BaseModel):
    id_dokumen: int
    judul: str
    kategori: str
    is_rahasia: bool
    tags: Optional[List[str]] = None

    json_kotor: ClassVar[dict] = {
        "id_dokumen": "105",      
        "judul": "Laporan Q1",
        "kategori": "Keuangan",
        "is_rahasia": "yes",  
        "tags": ["audit", 2026]
    }

print("--- START VALIDASI PAYLOAD DOKUMEN ---")

try:
    dokumen_valid = PayloadDokumen(**PayloadDokumen.json_kotor)
    print("[SUCCESS] Data berhasil divalidasi dan di-parsing!")
    print(f"ID (Tipe: {type(dokumen_valid.id_dokumen)}): {dokumen_valid.id_dokumen}")
    print(f"Rahasia (Tipe: {type(dokumen_valid.is_rahasia)}): {dokumen_valid.is_rahasia}")
    print(f"Tags: {dokumen_valid.tags}")

except ValidationError as e:
    print("[ERROR] Validasi Gagal! Payload dari Frontend tidak sesuai standar.")
    print(e)