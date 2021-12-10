import currencies
import ExchangeRates
from datetime import datetime, timedelta
from flask_restful import Resource, reqparse

# Front Facing API that handles currency conversion
class ExchangeRateConvertor(Resource):
	def get(self):
		parser = reqparse.RequestParser()
		parser.add_argument('from', type=str)
		parser.add_argument('to', type=str)
		parser.add_argument('amount', type=str)
		input_params = parser.parse_args()
		if "from" not in input_params:
		print("from error")
		#error handling
		if "to" not in input_params:
		#error handling
		if "amount" not in input_params:
		pass
		#error handling
		from_currency = input_params["from"]
		to_currency = input_params["to"]
		amount = input_params["amount"]

		# ERROR handling for unsupported currencies
		# Error handling for amount not a integer value

		print(input_params)
		response = predictive_exchange_rate_conversion(from_currency=from_currency,to_currency=to_currency,amount=amount)
		#convertor = publicapi_currencyexchange.ProcessExchangeRates(date="latest", from_currency=from_currency,to_currency=to_currency,amount=amount)
		return response

		#Function to call today's rate API and previous working day's API and forecast next_day's rate and provide it as output
	def predictive_exchange_rate_conversion(from_currency,to_currency,amount):
		# Todo
		# Include explation for logic calling multiple API and processing the result

		today_convertor = publicapi_currencyexchange.ProcessExchangeRates(date="latest", from_currency=from_currency,to_currency=to_currency,amount=amount)
		today_rate=today_convertor.get()
		print today_rate['rates'][to_currency]
		date_minus_2 = (datetime.today() - timedelta(days=2)).strftime("%Y-%m-%d")
		date_minus_4 = (datetime.today() - timedelta(days=4)).strftime("%Y-%m-%d")
		date_minus_6 = (datetime.today() - timedelta(days=6)).strftime("%Y-%m-%d")
		convertor_t2b = publicapi_currencyexchange.ProcessExchangeRates(date=date_minus_2, 		from_currency=from_currency,to_currency=to_currency,amount=amount)
		t2b_rate = convertor_t2b.get()
		convertor_t4b = publicapi_currencyexchange.ProcessExchangeRates(date=date_minus_4, from_currency=from_currency,to_currency=to_currency,amount=amount)
		t4b_rate = convertor_t4b.get()
		convertor_t6b = publicapi_currencyexchange.ProcessExchangeRates(date=date_minus_6, from_currency=from_currency,to_currency=to_currency,amount=amount)
		t6b_rate = convertor_t6b.get()
		predictive_rate = (t2b_rate['rates'][to_currency] + t4b_rate['rates'][to_currency]+ t6b_rate['rates'][to_currency])/3
		currency = publicapi_currencies.Currency()
		    currency_details = currency.get()
		response = {"From Currency":currency_details[from_currency], "To Currency":currency_details[to_currency], "Input Amount": amount, "Today's Value": today_rate['rates'][to_currency], "Predictive Tommorrow Value": predictive_rate }
		return response

