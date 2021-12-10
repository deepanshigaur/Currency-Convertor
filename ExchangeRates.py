import requests

class ProcessExchangeRates:
	def __init__(self, date, from_currency, to_currency, amount):
		self.api_url = "https://api.frankfurter.app/" + date + "?from=" + from_currency + "&to=" + to_currency + "&amount=" + amount
		self.resp_data = None
		self.process_data = None
        
	def get(self):
		response = requests.get(self.api_url)
		self.resp_data = response.json()
		return self.resp_data

	def process(self):
		print("dummy")

