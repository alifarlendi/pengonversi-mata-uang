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
    "USD": {"EUR": 0.84, "IDR": 14105.50},
    "EUR": {"USD": 1.19, "IDR": 16726.95},
    "IDR": {"USD": 0.000071, "EUR": 0.000060}
}

print("Selamat datang di Konverter Mata Uang!")
jumlah = float(input("\nMasukkan jumlah uang: "))
mata_uang_asal = input("Masukkan mata uang asal (misal: USD, EUR, IDR): ").upper()
mata_uang_tujuan = input("Masukkan mata uang tujuan (misal: USD, EUR, IDR): ").upper()

# Metode dengan return type
konverter = KonversiMataUang(kurs_pertukaran)
jumlah_konversi = konverter.konversi_mata_uang(jumlah, mata_uang_asal, mata_uang_tujuan)
print(f"Jumlah yang dikonversi: {jumlah_konversi} {mata_uang_tujuan}")  # Menampilkan mata uang tujuan di samping jumlah konversi

# Metode dengan non-return type
konverter.tampilkan_kurs_pertukaran()

print("\nDibuat oleh KELOMPOK 22")