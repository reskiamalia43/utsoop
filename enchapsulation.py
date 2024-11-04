class Siswa:
    def __init__(self, nama, nilai, kelas_siswa):
        self.nama = nama
        self.__nilai = nilai  
        self.kelas_siswa = kelas_siswa

    def get_nilai(self):
        return self.__nilai

    def set_nilai(self, nilai_baru):
        if 0 <= nilai_baru <= 100:
            self.__nilai = nilai_baru
        else:
            print("Nilai harus berada di antara 0 dan 100.")

    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Kelas: {self.kelas_siswa}")
        print(f"Nilai: {self.get_nilai()}") 

siswa1 = Siswa("Amalia", 99, "Si1(A)")

siswa1.display_info()
siswa1.set_nilai(100)
print("\nSetelah pembaruan nilai:")
siswa1.display_info()
