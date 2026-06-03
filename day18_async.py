import asyncio
import time

async def get_data_user():
   print("[SERVER] Mengambil profil user dari Database (Butuh 2 detik)...")
   await asyncio.sleep(2)
   print("[SERVER] Profil user berhasil diambil.")
   return {"user": "Joko", "role": "Admin"}

async def clasification_docs_ai():
    print("[AI_SERVICE] Memulai ekstraksi teks dokumen (Butuh 3 detik)...")
    await asyncio.sleep(3)
    print("[AI_SERVICE] Dokumen berhasil diklasifikasikan sebagai: KEUANGAN")
    return "KEUANGAN"

async def main():
    print("--- MEMULAI PROSES PARALEL ---")
    start_time = time.time()
    task1 = asyncio.create_task(get_data_user())
    task2 = asyncio.create_task(clasification_docs_ai())
    hasil_user = await task1
    hasil_ai = await task2
    end_time = time.time()
    print(f"Hasil User: {hasil_user}")
    print(f"Hasil AI: {hasil_ai}")
    selesai = time.perf_counter()
    print(f"Total waktu eksekusi: {end_time - start_time:.2f} detik")


if __name__ == "__main__":
    asyncio.run(main())