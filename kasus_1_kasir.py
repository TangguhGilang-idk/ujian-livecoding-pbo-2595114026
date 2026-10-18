#Studi Kasus 1 Kasir
class TransaksiKasir:
    def __init__(self, pelanggan, barang, harga_satuan, jumlah):
        self.pelanggan = pelanggan
        self.barang = barang


        if harga_satuan > 0:
            self.harga_satuan = harga_satuan
        else:
            self.harga_satuan = 0 

        if jumlah > 0:
            self.jumlah = jumlah
        else:
            self.jumlah = 0


    def hitung_subtotal(self):
        return self.harga_satuan * self.jumlah


    def tentukan_diskon(self, subtotal):
        if subtotal >= 500000:
            return 0.15
        elif subtotal >= 250000:
            return 0.10
        elif subtotal >= 100000:
            return 0.05
        else:
            return 0.0


    def tampilkan_struk(self):
        subtotal = self.hitung_subtotal()
        persen_diskon = self.tentukan_diskon(subtotal)
        potongan = int(subtotal * persen_diskon)
        total_bayar = subtotal - potongan

        print("=== STRUK PEMBAYARAN ===")
        print(f"Pelanggan\t: {self.pelanggan}")
        print(f"Barang\t\t: {self.barang}")
        print(f"Subtotal\t: Rp{subtotal}")
        print(f"Diskon\t\t: {int(persen_diskon * 100)}%")
        print(f"Potongan\t: Rp{potongan}")
        print(f"Total Bayar\t: Rp{total_bayar}")
        print("=========================")


print("=== KASIR MINIMARKET ===")
nama_pelanggan = input("Nama Pelanggan: ")
nama_barang = input("Nama Barang: ")
harga_barang = int(input("Harga Barang: "))
jumlah_barang = int(input("Jumlah Barang: "))


transaksi = TransaksiKasir(nama_pelanggan, nama_barang, harga_barang, jumlah_barang)
transaksi.tampilkan_struk()