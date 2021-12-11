import currencyexchange
import currencies
import consts

def validateInputCurrencies(from_currency, to_currency): 
    # Error handling if the currency is of supported one's
    if from_currency.upper() not in consts.SUPPORTED_CURRENCIES:
       print("Unsupported or Invalid From Currency Symbol: ", from_currency)
       print("Supported Currencies: ", consts.SUPPORTED_CURRENCIES)
       return False
    elif to_currency.upper() not in consts.SUPPORTED_CURRENCIES:
       print("Unsupported or Invalid to Currency Symbol: ", to_currency)
       print("Supported Currencies: ", consts.SUPPORTED_CURRENCIES)
       return False
    return True

def validateInputAmount(amount):
    # Error handling for amount not a proper value
    try:
        float(amount)
        return True
    except:
        print("Entered amount is not a proper value: ", amount)
        return False

def main():
   exchanger = currencyexchange.ProcessExchangeRates()
   currency_data = currencies.Currency()
   print("Currency Convertor")
   from_currency = input("Enter from Currency(Ex. USD): ")
   to_currency = input("Enter to Currency(Ex. EUR): ")
   amount = input("Amount to be converted: ")
   if validateInputAmount(amount) & validateInputCurrencies(from_currency, to_currency):
        if exchanger.get(from_currency=from_currency, to_currency=to_currency, amount=amount):
            if currency_data.get(): 
                    output_sting = "\nConversion value from " + currency_data.resp_data[from_currency.upper()] + \
                        " to " + currency_data.resp_data[to_currency.upper()] + " is " \
                            +  str(exchanger.resp_data['rates'][to_currency.upper()]) + "\n"
            print(output_sting)

if __name__ == "__main__":
    main()


