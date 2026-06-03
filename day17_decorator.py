sesi_user = {
    "username": "joko",
    "is_logged_in": False
}

def login_required(fungsi_asli):
    def wrapper(*args, **kwargs):
        print(f"[MIDDLEWARE] Mengecek sesi untuk {sesi_user['username']}...")
        if sesi_user["is_logged_in"]:
            print("[MIDDLEWARE] Sesi valid. Melanjutkan ke fungsi utama.")
            return fungsi_asli(*args, **kwargs)
        else:
            print("[MIDDLEWARE] Sesi tidak valid. Akses ditolak.")
            return "Error: Anda harus login untuk mengakses fungsi ini."
    return wrapper
    
@login_required
def proses_checkout(total_bayar):
    print(f"[SYSTEM] Memproses pembayaran sebesar Rp {total_bayar}...")
    print("[SYSTEM] Checkout Berhasil! Saldo terpotong.")

@login_required
def lihat_profil():
    print(f"[SYSTEM] Menampilkan data pribadi milik {sesi_user['username']}")


print("--- PERCOBAAN 1: BELUM LOGIN ---")
proses_checkout(5000000)

print("\n--- PERCOBAAN 2: SETELAH LOGIN ---")
sesi_user["is_logged_in"] = True

proses_checkout(5000000)
lihat_profil()