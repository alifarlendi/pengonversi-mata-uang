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
        print("--------------------------------------------")
        print(f"Kurs Pertukaran - Hari ini ({tanggal_hari_ini}):")
        for mata_uang, rates in self.kurs_pertukaran.items():
            print(mata_uang + ":")
            for mata_uang_tujuan, rate in rates.items():
                print(f"  1 {mata_uang} = {rate} {mata_uang_tujuan}")

kurs_pertukaran = {
    "USD": {"IDR": 14105.50, "GBP": 0.79, "JPY": 151.34, "AUD": 1.53},
    "GBP": {"USD": 1.26, "IDR": 20046.24, "JPY": 191.05, "AUD": 1.94},
    "JPY": {"USD": 0.0066, "IDR": 104.86, "GBP": 0.0052, "AUD": 0.010},
    "AUD": {"USD": 0.65, "GBP": 0.52, "JPY": 98.78},
    "IDR": {"USD": 0.000071, "GBP": 0.000050, "JPY": 0.0095, "AUD": 0.000097}
}

print("Selamat datang di Konverter Mata Uang!")
print("--------------------------------------")
jumlah = float(input("Masukkan Jumlah Uang Anda: "))


print("\nPilih Mata Uang Asal:")
for mata_uang in kurs_pertukaran.keys():
    print("- ", mata_uang)

mata_uang_asal = input("Masukkan Mata Uang Asal (Contoh: IDR): ").upper()

print("------------------------------------------")

print("Pilih Mata Uang Tujuan:")
for mata_uang in kurs_pertukaran.keys():
    print("- ", mata_uang)

mata_uang_tujuan = input("Masukkan Mata Uang Tujuan (Contoh: USD): ").upper()

konverter = KonversiMataUang(kurs_pertukaran)
jumlah_konversi = konverter.konversi_mata_uang(jumlah, mata_uang_asal, mata_uang_tujuan)

print(f"\nJumlah yang dikonversi: {jumlah_konversi} {mata_uang_tujuan}")

konverter.tampilkan_kurs_pertukaran()

print("\nProgram Selesai")
print("\nDibuat oleh KELOMPOK 22")
