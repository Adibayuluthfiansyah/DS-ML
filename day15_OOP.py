import json

class KeranjangBelanja:
    def __init__(self, nama_user):
        self.nama_user = nama_user
        self.items = [] 
        print(f"[*] Keranjang baru dibuat untuk: {self.nama_user}")

    def tambah_item(self, nama_barang, harga):
        self.items.append({"nama": nama_barang, "harga": harga})
        print(f"+ Ditambahkan: {nama_barang} (Rp {harga})")

    def hitung_total(self):
        total = 0
        for item in self.items:
            total += item["harga"]
        return total

    def simpan_ke_db(self):
        nama_file = f"db_{self.nama_user}.json"
        try:
            with open(nama_file, "w") as f:
                json.dump(self.items, f)
                print(f"[*] Data {self.nama_user} berhasil disimpan ke {nama_file}")
        except Exception as e:
            print(f"[!] Gagal menyimpan data: {e}")



cart_ihza = KeranjangBelanja("Ihza")
cart_tamu = KeranjangBelanja("Guest_001")


cart_ihza.tambah_item("Laptop RTX", 15000000)
cart_ihza.tambah_item("Mouse Pad", 150000)


cart_tamu.tambah_item("Kabel Type-C", 50000)


print(f"Total tagihan Ihza: Rp {cart_ihza.hitung_total()}")
print(f"Total tagihan Tamu: Rp {cart_tamu.hitung_total()}")

cart_ihza.simpan_ke_db()
cart_tamu.simpan_ke_db()