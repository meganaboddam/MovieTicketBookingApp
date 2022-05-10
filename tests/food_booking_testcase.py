__author__ = 'Sahana Pandurangi Raghavendra'
__author__ = 'Megana Reddy Boddam'

import unittest
from food_booking_lib import *
import unittest

# urls / API endpoints used by food booking lambda service
url_list_of_pickup_times = "https://9qhi5gewy6.execute-api.us-east-1.amazonaws.com/prod/pickuptime"
url_list_of_food = "https://9qhi5gewy6.execute-api.us-east-1.amazonaws.com/prod/listoffood"

# headers
headers_with_apikey = {'Content-type': 'application/json', 'Accept': 'application/json',
                        'x-api-key': 'ynbWkSO7m32Mk64vd2d7NaD6VyYm8D1fH18A01O9'}
headers_no_apikey = {'Content-type': 'application/json', 'Accept': 'application/json'}

# Testcases that test all the endpoints pertaining to food booking lambda interfaces.
class FoodBookingTestcases(unittest.TestCase):
    def get_list_of_food_positive_test_one(self):
        general_obj = FoodBooking()
        status_code, response_json = general_obj.get_list_of_food(url_list_of_food, {'user_id': 1, 'theater_id': 1},
                                                          headers_with_apikey)
        print("status code is: " + str(status_code))
        self.assertEqual(status_code, 200)
        print("the response is: " + str(response_json))
        print("Checking First Food")
        actual_val = response_json['food'][0]['food_name']
        self.assertEqual(str(actual_val), "Butter Popcorn (Small)", "ERR: Failed to get appropriate food")
        print("Checking Second Food")
        actual_val = response_json['food'][1]['food_name']
        self.assertEqual(str(actual_val), "Butter Popcorn (Medium)", "ERR: Failed to get appropriate food")
        print("Checking Third Food")
        actual_val = response_json['food'][2]['food_name']
        self.assertEqual(str(actual_val), "Butter Popcorn (Large)", "ERR: Failed to get appropriate food")


    def get_list_of_food_negative_test_one(self):
        general_obj = FoodBooking()
        status_code, response_json = general_obj.get_list_of_food(url_list_of_food, {'user_id': 1, 'theater_id': 1},
                                                          headers_no_apikey)
        print("status code is: " + str(status_code))
        self.assertEqual(status_code, 403)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Forbidden", "ERR: Failed to get the appropriate negative response")

    def post_selected_food_positive_test_one(self):
        general_obj = FoodBooking()
        status_code, response_json = general_obj.post_food(url_list_of_food,
                                                           {'user_id': 1, 'booking_id': 1, 'food_id': 1, 'quantity': 1},
                                                           headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        print("Checking if posted correct food name")
        actual_val = response_json['food_name']
        self.assertEqual(str(actual_val), "Butter Popcorn (Small)", "ERR: Failed to post the appropriate food")
        print("Checking if posted correct food quantity")
        actual_val = response_json['quantity']
        self.assertEqual(str(actual_val), "1", "ERR: Failed to post the appropriate food")

    def post_selected_food_negative_test_one(self):
        general_obj = FoodBooking()
        status_code, response_json = general_obj.post_food(url_list_of_food, None,
                                                           headers_no_apikey)
        print(status_code)
        self.assertEqual(status_code, 403)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Forbidden", "ERR: Failed to get the appropriate negative response")

    def get_list_of_pickup_times_positive_test_one(self):
        general_obj = FoodBooking()
        status_code, response_json = general_obj.get_pickup_times(url_list_of_pickup_times,
                                                                  {'user_id': 1, 'booking_id': 1},
                                                                  headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        print("Checking First PickUp Time")
        actual_val = response_json[0]['pickup_time']
        self.assertEqual(str(actual_val), "12:00:00", "ERR: Failed to get the appropriate pickup time")
        print("Checking Second PickUp Time")
        actual_val = response_json[1]['pickup_time']
        self.assertEqual(str(actual_val), "12:05:00", "ERR: Failed to get the appropriate pickup time")
        print("Checking Third PickUp Time")
        actual_val = response_json[2]['pickup_time']
        self.assertEqual(str(actual_val), "12:10:00", "ERR: Failed to get the appropriate pickup time")

    def get_list_of_pickup_times_negative_test_one(self):
        general_obj = FoodBooking()
        status_code, response_json = general_obj.get_pickup_times(url_list_of_pickup_times,
                                                                  {'user_id': 1, 'booking_id': 1},
                                                                  headers_no_apikey)
        print(status_code)
        self.assertEqual(status_code, 403)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Forbidden", "ERR: Failed to get the appropriate negative response")

    def post_selected_pickup_time_positive_test_one(self):
        general_obj = FoodBooking()
        status_code, response_json = general_obj.post_pickup_times(url_list_of_pickup_times,
                                                                   {'user_id': 1, 'booking_id': 1,
                                                                    'pickup_time': '12:00:00'},
                                                                   headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['pickup_time']
        self.assertEqual(str(actual_val), "12:00:00", "ERR: Failed to post the appropriate pickup time")

    def post_selected_pickup_time_negative_test_one(self):
        general_obj = FoodBooking()
        status_code, response_json = general_obj.post_pickup_times(url_list_of_pickup_times, None,
                                                                   headers_no_apikey)
        print(status_code)
        self.assertEqual(status_code, 403)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Forbidden", "ERR: Failed to get the appropriate negative response")


