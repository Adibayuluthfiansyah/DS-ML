class KeranjangBelanja:
    def __init__(self, nama_user):
        self.nama_user = nama_user
        self.items = []
    def tambah_item(self, nama_barang,harga):
        self.items.append({"nama": nama_barang, "harga": harga})
    def hitung_total(self):
            total = 0 
            for item in self.items:
                total += item["harga"]
            return total
        

class KeranjangBelanjaVIP(KeranjangBelanja):
    def hitung_total(self):
        total_asli = super().hitung_total()
        total_diskon = total_asli * 0.9
        print(f"[*] {self.nama_user} mendapatkan diskon VIP 10%!")
        return int(total_diskon) 
    
cart_reguler = KeranjangBelanja("Reguler_User")
cart_reguler.tambah_item("Monitor 4K", 5000000)


cart_vip = KeranjangBelanjaVIP("Sultan_VIP")
cart_vip.tambah_item("Monitor 4K", 5000000)

print(f"Tagihan Reguler: Rp {cart_reguler.hitung_total()}")
print(f"Tagihan VIP    : Rp {cart_vip.hitung_total()}")
        