from datetime import datetime

class KonversiMataUang:
    def __init__(self, kurs_pertukaran):
        self.kurs_pertukaran = kurs_pertukaran

    def konversi_mata_uang(self, jumlah, mata_uang_asal, mata_uang_tujuan):
        if mata_uang_asal == mata_uang_tujuan:
            print("Sama mata uangnya, tidak perlu konversi.")
            return jumlah

        jumlah_konversi = jumlah * self.kurs_pertukaran[mata_uang_asal][mata_uang_tujuan]
        return jumlah_konversi

    def tampilkan_kurs_pertukaran(self):
        tanggal_hari_ini = datetime.now().strftime("%d-%m-%Y")
        print(f"\nKurs Pertukaran - Hari ini ({tanggal_hari_ini}):")
        for mata_uang, rates in self.kurs_pertukaran.items():
            print(mata_uang + ":")
            for mata_uang_tujuan, rate in rates.items():
                print(f"  1 {mata_uang} = {rate} {mata_uang_tujuan}")

def konversi_mata_uang(jumlah, kurs_pertukaran, mata_uang_asal, mata_uang_tujuan):
    if mata_uang_asal == mata_uang_tujuan:
        print("Sama mata uangnya, tidak perlu konversi.")
        return jumlah

    jumlah_konversi = jumlah * kurs_pertukaran[mata_uang_asal][mata_uang_tujuan]
    print(f"{jumlah} {mata_uang_asal} sama dengan {jumlah_konversi} {mata_uang_tujuan}")

def tampilkan_kurs_pertukaran(kurs_pertukaran):
    tanggal_hari_ini = datetime.now().strftime("%d-%m-%Y")
    print(f"Kurs Pertukaran - Hari ini ({tanggal_hari_ini}):")
    for mata_uang, rates in kurs_pertukaran.items():
        print(mata_uang + ":")
        for mata_uang_tujuan, rate in rates.items():
            print(f"  1 {mata_uang} = {rate} {mata_uang_tujuan}")


kurs_pertukaran = {
    "USD": {"EUR": 0.93, "IDR": 15880.10, "JPY": 151.34, "CAD": 1.35, "GBP": 0.79, "AUD": 1.53},
    "EUR": {"USD": 1.08, "IDR": 17151.30, "JPY": 163.57, "CAD": 1.46, "GBP": 0.86, "AUD": 1.66},
    "IDR": {"USD": 0.000063, "EUR": 0.000060, "JPY": 0.0095, "CAD": 0.000085, "GBP": 0.000050, "AUD": 0.000097},
    "JPY": {"USD": 0.0066, "IDR": 104.86, "EUR": 0.0061, "CAD": 0.0089, "GBP": 0.0052, "AUD": 0.010},
    "CAD": {"USD": 0.74, "IDR": 11745.77, "EUR": 0.69, "JPY": 112.03, "GBP": 0.59, "AUD": 1.14},
    "GBP": {"USD": 1.26, "IDR": 20046.24, "EUR": 1.17, "JPY": 191.05, "AUD": 1.94, "CAD": 1.71},
    "AUD": {"USD": 0.65, "IDR": 10352.24, "EUR": 0.60, "JPY": 98.78, "GBP": 0.52, "CAD": 0.88}
}

I = ["1. AUD", '2. CAD', '3. EUR', '4. GBP', '5. IDR', '6. JPY', '7. USD']
print("Selamat datang di Konverter Mata Uang!")
jumlah = float(input("\nMasukkan Jumlah Uang Anda: "))
for kata in I :
    print(kata)
mata_uang_asal = input("Masukkan Mata Uang Asal (Contoh : IDR): ").upper()
for kata in I :
    print(kata)
mata_uang_tujuan = input("Masukkan Mata Uang Tujuan (Contoh : USD): ").upper()

# Metode dengan return type
konverter = KonversiMataUang(kurs_pertukaran)
jumlah_konversi = konverter.konversi_mata_uang(jumlah, mata_uang_asal, mata_uang_tujuan)
# Menampilkan mata uang tujuan di samping jumlah konversi
print(f"Jumlah yang dikonversi: {jumlah_konversi} {mata_uang_tujuan}")

# Metode dengan non-return type
konverter.tampilkan_kurs_pertukaran()

print("\nPROGRAM INI BERJALAN BERDASARKAN KURS PERTUKARAN UANG PADA TANGGAL 31 MARET 2024")
print("\nDibuat oleh KELOMPOK 22")
