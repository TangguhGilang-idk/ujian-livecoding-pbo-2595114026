#Studi kasus 1 Kasir
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

        print("\n=== STRUK PEMBAYARAN ===")
        print(f"Pelanggan\t: {self.pelanggan}")
        print(f"Barang\t\t: {self.barang}")
        print(f"Subtotal\t: Rp{subtotal}")
        print(f"Diskon\t\t: {int(persen_diskon * 100)}%")
        print(f"Potongan\t: Rp{potongan}")
        print(f"Total bayar\t: Rp{total_bayar}")
        print("=========================")


def input_teks_valid(pesan):
    """Memvalidasi bahwa masukan tidak kosong dan bukan angka."""
    while True:
        teks = input(pesan).strip()
        if not teks:
            print("Peringatan: Input teks tidak boleh kosong!")
        elif teks.isdigit():
            print("Peringatan: Teks tidak boleh hanya berupa angka!")
        else:
            return teks


def input_angka_positif(pesan):
    """Memvalidasi bahwa masukan berjenis angka positif."""
    while True:
        try:
            nilai = int(input(pesan))
            if nilai <= 0:
                print("Peringatan: Nilai harus berupa aangka bulat positif")
                continue
            return nilai
        except ValueError:
            print("Peringatan: Tipe data salah! Masukkan beupa angka bulat positif.")


print("=== KASIR MINIMARKET ===")
nama_pelanggan = input_teks_valid("Nama Pelanggan : ")
nama_barang    = input_teks_valid("Nama Barang     : ")
harga_barang   = input_angka_positif("Harga Barang     : ")
jumlah_barang  = input_angka_positif("Jumlah Barang  : ")


transaksi = TransaksiKasir(nama_pelanggan, nama_barang, harga_barang, jumlah_barang)
transaksi.tampilkan_struk()