class Kalkulator:
    def __init__(self):
        pass

    def penjumlahan(self):
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        return angka1 + angka2

    def pengurangan(self):
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        return angka1 - angka2

    def perkalian(self):
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        return angka1 * angka2

    def pembagian(self):
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        if angka2 != 0:
            return angka1 / angka2
        else:
            return "Error: Pembagian dengan nol tidak diperbolehkan."

# Contoh penggunaan
kalkulator = Kalkulator()

print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan = input("Pilih operasi (1/2/3/4): ")

if pilihan == '1':
    print("Hasil penjumlahan:", kalkulator.penjumlahan())
elif pilihan == '2':
    print("Hasil pengurangan:", kalkulator.pengurangan())
elif pilihan == '3':
    print("Hasil perkalian:", kalkulator.perkalian())
elif pilihan == '4':
    print("Hasil pembagian:", kalkulator.pembagian())
else:
    print("Pilihan tidak valid")
