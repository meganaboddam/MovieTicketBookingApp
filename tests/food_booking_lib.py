__author__ = 'Sahana Pandurangi Raghavendra', 'Megana Reddy Boddam'

# importing api methods file that contain the GET and POST library code
from requests import post

from apimethodslib import *


# Class that implements all libraries to test the API ends pertaining Food booking lambda service
class FoodBooking:

    def __init__(self):
        self.methods_api = APIMethodsLib()

    # Function to test the API that queries the database for a list available
    # food items for consumption during movie
    # input : url / api endpoint to which request has to be sent
    # params: query string parameters that has to be sent with the API request
    # headers: headers that need to be added for that API
    def get_list_of_food(self, request_url, params=None, headers=None):
        print("Getting the list of available food and beverages for consumption during movie")
        response = self.methods_api.get(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        print(response_json)
        return status_code, response_json

    # Function to test the API that posts the selected food and beverages by the customer
    # input : url / api endpoint to which request has to be sent
    # params: query string parameters that has to be sent with the API request
    # headers: headers that need to be added for that API
    def post_food(self, request_url, params=None, headers=None):
        print("Posting the selected food and beverages")
        response = post(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        print(response_json)
        return status_code, response_json

    # Function to test the API that queries for the list of available
    # times for picking up the food/beverages before movie
    # input : url / api endpoint to which request has to be sent
    # params: query string parameters that has to be sent with the API request
    # headers: headers that need to be added for that API
    def get_pickup_times(self, request_url, params=None, headers=None):
        print("Getting the list of available times for picking up the food/beverages before movie")
        response = self.methods_api.get(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        print(response_json)
        return status_code, response_json

    # Function to test the API that posts the selected time for picking up food.
    # input : url / api endpoint to which request has to be sent
    # params: query string parameters that has to be sent with the API request
    # headers: headers that need to be added for that API
    def post_pickup_times(self, request_url, params=None, headers=None):
        print("Posting the selected time for picking up food")
        response = post(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        print(response_json)
        return status_code, response_json
