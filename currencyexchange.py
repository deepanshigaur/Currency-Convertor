import requests

class ProcessExchangeRates:
   
    def __init__(self):
        self.api_url = "https://api.frankfurter.app/latest"
        self.resp_data = None

    def get(self, from_currency, to_currency, amount):
        try:
            params = {'from': from_currency, 'to': to_currency, 'amount':amount}
            response = requests.get(self.api_url, params=params, timeout=5)
            self.resp_data = response.json()
            return True

        except:
            print("Check internet: Public API call Failed")
            return False


