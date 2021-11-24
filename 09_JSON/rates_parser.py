import json


# On initialisation, take path to file
# Base, date, GDB, USD, AUD,
# Rates: dict
# Method called convert string new_currency:str value_euro:float -> float
# Handle currencies not in json files


class RatesParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_info = self._parse_exchange_rates()
        self.base = self.file_info["base"]
        self.date = self.file_info["date"]
        self.gbp_rate = self.file_info["rates"]["GBP"]
        self.usd_rate = self.file_info["rates"]["USD"]
        self.aud_rate = self.file_info["rates"]["AUD"]
        self.rates = self.file_info["rates"]

    def _parse_exchange_rates(self):
        with open(self.file_path) as file:
            return json.load(file)

    def convert_base_currency(self, convert_to: str, amount_in_euros: float) -> float:
        if convert_to in self.rates.keys():
            return round(amount_in_euros * self.rates[convert_to], 2)

        while True:
            add_currency = input("Would you like to add this new currency? (y/n)\n")
            if add_currency == "y":
                self.add_new_currency(convert_to)
                break
            if add_currency == "n":
                break
            print("Please enter y or n...\n")

    def add_new_currency(self, new_currency):
        new_rate = input("Enter exchange rate:\n")
        with open(self.file_path, "w") as file:
            self.file_info["rates"][new_currency] = float(new_rate)
            json.dump(self.file_info, file)


r = RatesParser("exchange_rates.json")

print(type(r.file_info))

print(r.convert_base_currency("AUD", 10))

r.convert_base_currency("Gold", 1000)
