class PengirimanBarang:
    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat

    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi

    def hitung_harga(self):
        volume = self.hitung_volume()
        if volume < 50:
            volume = 50  # Menggunakan volume minimal 50 cm kubik
        berat = self.berat
        if berat < 1:
            berat = 1  # Menggunakan berat minimal 1 kg

        harga_per_kg = 5000
        harga_dimensi = volume * harga_per_kg / 50  # Harga proporsional terhadap volume
        harga_berat = berat * harga_per_kg

        return max(harga_dimensi, harga_berat)  # Mengambil harga terbesar dari keduanya

panjang = float(input("Masukkan panjang barang (cm): "))
lebar = float(input("Masukkan lebar barang (cm): "))
tinggi = float(input("Masukkan tinggi barang (cm): "))
berat = float(input("Masukkan berat barang (kg): "))

pengiriman = PengirimanBarang(panjang, lebar, tinggi, berat)
harga_pengiriman = pengiriman.hitung_harga()

print(f"Harga pengiriman barang adalah: Rp. {harga_pengiriman:,}")
