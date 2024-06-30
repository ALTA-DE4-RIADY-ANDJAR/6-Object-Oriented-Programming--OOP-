
#Challenge 1

#Hitung Luas Keliling

#Hitung Persegi
class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2

    def hitung_keliling(self):
        return 4 * self.sisi

sisi_persegi = float(input("Masukkan panjang sisi persegi: "))
persegi = Persegi(sisi_persegi)
print("Luas persegi:", persegi.hitung_luas())
print("Keliling persegi:", persegi.hitung_keliling())


#Hitung Segitiga
class Segitiga:
    def __init__(self, alas, tinggi, sisi1, sisi2, sisi3):
        self.alas = alas
        self.tinggi = tinggi
        self.sisi1 = sisi1
        self.sisi2 = sisi2
        self.sisi3 = sisi3

    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

    def hitung_keliling(self):
        return self.sisi1 + self.sisi2 + self.sisi3

alas = float(input("Masukkan panjang alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))
sisi1 = float(input("Masukkan panjang sisi pertama segitiga: "))
sisi2 = float(input("Masukkan panjang sisi kedua segitiga: "))
sisi3 = float(input("Masukkan panjang sisi ketiga segitiga: "))
segitiga = Segitiga(alas, tinggi, sisi1, sisi2, sisi3)
print("Luas segitiga:", segitiga.hitung_luas())
print("Keliling segitiga:", segitiga.hitung_keliling())


#Hitung Persegi Panjang
class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))
persegi_panjang = PersegiPanjang(panjang, lebar)
print("Luas persegi panjang:", persegi_panjang.hitung_luas())
print("Keliling persegi panjang:", persegi_panjang.hitung_keliling())



    
