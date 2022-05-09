from api_methods_lib import *


class PaymentProcessing:

    def __init__(self):
        self.methods_api = Apimethods()

    def post_booking_cost(self, request_url, params=None, headers=None):
        print("Posting the booking cost")
        response = self.methods_api.post(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        logging.Logger(response_json)
        return status_code, response_json

    def get_booking_cost(self, request_url, params=None, headers=None):
        print("Getting the total cost of booked show and food/beverages")
        response = self.methods_api.get(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        logging.Logger(response_json)
        return status_code, response_json

    def get_tickets(self, request_url, params=None, headers=None):
        print("Getting the list of booked tickets")
        response = self.methods_api.get(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        logging.Logger(response_json)
        return status_code, response_json
