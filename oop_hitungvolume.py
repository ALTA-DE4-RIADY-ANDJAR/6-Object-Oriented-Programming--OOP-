
#Hitung Volume Kubus

class Kubus:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_volume(self):
        return self.sisi ** 3

sisi_kubus = float(input("Masukkan panjang sisi kubus: "))
kubus = Kubus(sisi_kubus)
print("Volume kubus:", kubus.hitung_volume())



#Hitung Volume Balok

class Balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi

panjang_balok = float(input("Masukkan panjang balok: "))
lebar_balok = float(input("Masukkan lebar balok: "))
tinggi_balok = float(input("Masukkan tinggi balok: "))
balok = Balok(panjang_balok, lebar_balok, tinggi_balok)
print("Volume balok:", balok.hitung_volume())



#Hitung Volume Tabung

import math

class Tabung:
    def __init__(self, jari_jari, tinggi):
        self.jari_jari = jari_jari
        self.tinggi = tinggi

    def hitung_volume(self):
        return math.pi * self.jari_jari ** 2 * self.tinggi

jari_jari_tabung = float(input("Masukkan jari-jari tabung: "))
tinggi_tabung = float(input("Masukkan tinggi tabung: "))
tabung = Tabung(jari_jari_tabung, tinggi_tabung)
print("Volume tabung:", tabung.hitung_volume())


