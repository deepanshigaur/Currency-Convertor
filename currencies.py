import requests

class Currency:

    def __init__(self):
        self.api_url = "https://api.frankfurter.app/currencies"
        self.resp_data = None
        
    def get(self):
        try:
            response = requests.get(self.api_url, timeout=5)
            self.resp_data = response.json()
            return True

        except:
            print("Check internet: Public API call Failed")
            return False

