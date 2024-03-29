class CurrencyConverter:
    def __init__(self):
        self.exchange_rates = {
            'USD': {'IDR': 14000, 'EUR': 0.85},
            'IDR': {'USD': 0.000071, 'EUR': 0.000061},
            'EUR': {'USD': 1.18, 'IDR': 16429}
        }

    def get_exchange_rate(self, base_currency, target_currency):
        if base_currency in self.exchange_rates and target_currency in self.exchange_rates[base_currency]:
            return self.exchange_rates[base_currency][target_currency]
        else:
            print("Maaf, nilai tukar tidak tersedia.")

    def convert_currency(self, amount, base_currency, target_currency):
        exchange_rate = self.get_exchange_rate(base_currency, target_currency)
        if exchange_rate is not None:
            converted_amount = amount * exchange_rate
            print(f"{amount} {base_currency} setara dengan {converted_amount} {target_currency}")
        else:
            print("Maaf, nilai tukar tidak tersedia.")

def main():
    print("Selamat datang di Aplikasi Pengonversi Mata Uang!")
    converter = CurrencyConverter()
    base_currency = input("Masukkan kode mata uang asal (misal: USD, EUR, IDR): ").upper()
    target_currency = input("Masukkan kode mata uang tujuan (misal: USD, EUR, IDR): ").upper()
    amount = float(input("Masukkan jumlah uang yang ingin dikonversi: "))

    converter.convert_currency(amount, base_currency, target_currency)

if __name__ == "__main__":
    main()

print("\nDibuat oleh KELOMPOK 22")