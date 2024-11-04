class Hewan:
    def __init__(self, nama, jumlah_kaki):
        self.nama = nama
        self.jumlah_kaki = jumlah_kaki

    def info_Hewan(self):
        return f"Nama: {self.nama}, Jumlah_kaki: {self.jumlah_kaki}"
    
class Buaya(Hewan):
    def __init__(self, nama, jumlah_kaki, suara):
        super().__init__(nama, jumlah_kaki)
        self.suara = suara

    def info_Buaya(self):
        return f"Nama: {self.nama}, Jumlah_kaki: {self.jumlah_kaki}, suara:{self.suara}"  

class Monyet(Hewan):
    def __init__(self, nama, jumlah_kaki, makanan):
        super().__init__(nama, jumlah_kaki) 
        self.makanan = makanan

    def info_Monyet(self):
        return f"Nama: {self.nama}, Jumlah_kaki: {self.jumlah_kaki}, makakana: {self.makanan}"
    
siBuaya = Buaya("sudirman", 4, "hay cantik")
siMonyet = Monyet("kingkong", 2, "pisang")

print(siBuaya.info_Buaya())
print(siMonyet.info_Monyet())