class CurrencyConverter:
    def __init__(self):
        self.exchange_rates = {
            'USD': 1.0,
            'EUR': 0.84,
            'GBP': 0.76,
            'INR': 84.83,
            'AUD': 1.31,
            # Add more exchange rates as needed
        }

    def convert(self, from_currency, to_currency, amount):
        if from_currency != 'USD':
            amount = amount / self.exchange_rates[from_currency]

        return amount * self.exchange_rates[to_currency]


def main():
    converter = CurrencyConverter()

    print("Currency Converter")
    print("------------------")

    from_currency = input("From currency: ").upper()
    to_currency = input("To currency: ").upper()
    amount = float(input("Amount: "))

    result = converter.convert(from_currency, to_currency, amount)

    print(f"{amount} {from_currency} is equal to {result} {to_currency}")


if __name__ == "__main__":
    main()

