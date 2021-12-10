import currencyexchange
import currencies

def main():
   exchanger = currencyexchange.ProcessExchangeRates()
   currency_data = currencies.Currency()
   while True:
        print("Currency Convertor")
        from_currency = input("Enter from Currency(Ex. USD): ")
        to_currency = input("Enter to Currency(Ex. EUR): ")
        amount = input("Amount to be converted: ")
        exchanger.get(from_currency=from_currency, to_currency=to_currency, amount=amount)
        currency_data.get()
        output_sting = "\nConversion value from " + currency_data.resp_data[from_currency] + \
                       " to " + currency_data.resp_data[to_currency] + " is " \
                        +  str(exchanger.resp_data['rates'][to_currency]) + "\n"
        print(output_sting)

if __name__ == "__main__":
    main()

