from api_methods_lib import *


class FoodBooking:

    def __init__(self):
        self.methods_api = Apimethods()

    def get_list_of_food(self, request_url, params=None, headers=None):
        print("Getting the list of available food and beverages for consumption during movie")
        response = self.methods_api.get(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        logging.Logger(response_json)
        return status_code, response_json

    def post_food(self, request_url, params=None, headers=None):
        print("Posting the selected food and beverages")
        response = self.methods_api.post(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        logging.Logger(response_json)
        return status_code, response_json

    def get_pickup_times(self, request_url, params=None, headers=None):
        print("Getting the list of available times for picking up the food/beverages before movie")
        response = self.methods_api.get(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        logging.Logger(response_json)
        return status_code, response_json

    def post_pickup_times(self, request_url, params=None, headers=None):
        print("Posting the selected time")
        response = self.methods_api.post(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        logging.Logger(response_json)
        return status_code, response_json
