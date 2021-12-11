import requests

class Currency:

    def __init__(self):
        '''
    imports the first API
    args: self(class)
    return: None
        '''
        self.api_url = "https://api.frankfurter.app/currencies"
        self.resp_data = None
        
    def get(self):
        '''
    makes the response,takes the data and handles exceptions
    args: self(class)
    return: None
        '''
        try:
            response = requests.get(self.api_url, timeout=5)
            self.resp_data = response.json()
            return True

        except:
            print("Check internet: Public API call Failed")
            return False

