#Studi Kasus 2 Nilai Mahasiswa
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
        print(f"Nilai Akhir\t: {nilai_akhir:.2f}")
        print(f"Grade\t\t: {grade}")
        print(f"Status\t\t: {status}")
        print("=========================")

print("=== SISTEM PENILAIAN ===")
nim = input("NIM        : ")
nama = input("Nama       : ")
nilai_tugas = float(input("Nilai Tugas: "))
nilai_uts = float(input("Nilai UTS  : "))
nilai_uas = float(input("Nilai UAS  : "))

mahasiswa = PenilaianMahasiswa(nim, nama, nilai_tugas, nilai_uts, nilai_uas)
mahasiswa.cetak_hasil()