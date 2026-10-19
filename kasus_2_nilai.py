#Studi Kasus 2 Nilai
class PenilaianMahasiswa:
    def __init__(self, nim, nama, nilai_tugas, nilai_uts, nilai_uas):
        self.nim = nim
        self.nama = nama
        self.nilai_tugas = self.validasi_nilai(nilai_tugas)
        self.nilai_uts = self.validasi_nilai(nilai_uts)
        self.nilai_uas = self.validasi_nilai(nilai_uas)


    def validasi_nilai(self, nilai):
        if 0 <= nilai <= 100:
            return nilai
        return 0


    def hitung_nilai_akhir(self):
        return (self.nilai_tugas * 0.30) + (self.nilai_uts * 0.30) + (self.nilai_uas * 0.40)


    def tentukan_hasil(self, nilai_akhir):
        if nilai_akhir >= 85:
            grade = "A"
        elif nilai_akhir >= 75:
            grade = "B"
        elif nilai_akhir >= 65:
            grade = "C"
        elif nilai_akhir >= 50:
            grade = "D"
        else:
            grade = "E"

        status = "LULUS" if nilai_akhir >= 65 else "TIDAK LULUS"
        return grade, status


    def cetak_hasil(self):
        nilai_akhir = self.hitung_nilai_akhir()
        grade, status = self.tentukan_hasil(nilai_akhir)

        print("\n=== HASIL AKADEMIK ===")
        print(f"NIM\t\t: {self.nim}")
        print(f"Nama\t\t: {self.nama}")
        print(f"Nilai Akhir\t: {nilai_akhir}")
        print(f"Grade\t\t: {grade}")
        print(f"Status\t\t: {status}")
        print("========================")


def input_nim_valid(pesan):
    """Memvalidasi bahwa NIM tidak kosong dan hanya berisi angka."""
    while True:
        teks = input(pesan).strip()
        if not teks:
            print("Peringatan: NIM tidak boleh kosong!")
        elif not teks.isdigit():
            print("Peringatan: NIM harus berupa angka!")
        else:
            return teks


def input_nama_valid(pesan):
    """Memvalidasi bahwa nama tidak kosong."""
    while True:
        teks = input(pesan).strip()
        if not teks:
            print("Peringatan: Nama tidak boleh kosong!")
        elif teks.isdigit():
            print("Peringatan: Nama tidak boleh hanya berisi angka!")
        else:
            return teks


def input_nilai(pesan):
    """Memvalidasi angka float antara 0-100."""
    while True:
        try:
            nilai = float(input(pesan))
            if nilai < 0 or nilai > 100:
                print("Peringatan: Nilai harus berada dalam rentang 0-100!")
                continue
            return nilai
        except ValueError:
            print("Peringatan Tipe data salah! Masukkan angka desimal yang valid.")


print("=== SISTEM PENILAIAN ===")
nim         = input_nim_valid("NIM         : ")
nama        = input_nama_valid("Nama        : ")
nilai_tugas = input_nilai("Nilai Tugas : ")
nilai_uts   = input_nilai("Nilai UTS   : ")
nilai_uas   = input_nilai("Nilai UAS   : ")

mahasiswa = PenilaianMahasiswa(nim, nama, nilai_tugas, nilai_uts, nilai_uas)
mahasiswa.cetak_hasil()