katalog_produk = {
    "P001": {"nama": "Mechanical Keyboard", "harga": 850000},
    "P002": {"nama": "Wireless Mouse", "harga": 350000},
    "P003": {"nama": "Monitor 4K", "harga": 5000000}
}

keranjang = []


def tambah_ke_keranjang(id_produk):
    if id_produk in katalog_produk:
        keranjang.append(id_produk)
        print(f"{katalog_produk[id_produk]['nama']} berhasil ditambahkan ke keranjang.")
    else:
        print(f"Produk dengan ID '{id_produk}' tidak ditemukan dalam katalog.")

tambah_ke_keranjang("P001")
tambah_ke_keranjang("P003")
tambah_ke_keranjang("P999") 

def hitung_total(isi_keranjang):
    total = 0
    for id_produk in isi_keranjang:
        if id_produk in katalog_produk:
            total += katalog_produk[id_produk]['harga']
    
    return total


total_belanja = hitung_total(keranjang)
print(f"Total belanja Anda: Rp {total_belanja}")