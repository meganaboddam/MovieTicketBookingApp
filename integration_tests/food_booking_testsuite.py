import unittest
from food_booking_lib import *
import unittest

url_list_of_food = ""
headers_list_of_food = {'Content-type': 'application/json', 'Accept': 'application/json',
                        'x-api-key': ''}
headers_no_apikey_list_of_food = {'Content-type': 'application/json', 'Accept': 'application/json'}

url_post_selected_food = ""
headers_post_selected_food = {'Content-type': 'application/json', 'Accept': 'application/json',
                              'x-api-key': ''}
headers_no_apikey_post_selected_food = {'Content-type': 'application/json', 'Accept': 'application/json'}

url_list_of_pickup_times = ""
headers_list_of_pickup_times = {'Content-type': 'application/json', 'Accept': 'application/json',
                                'x-api-key': ''}
headers_no_apikey_list_of_pickup_times = {'Content-type': 'application/json', 'Accept': 'application/json'}

url_post_selected_pickup_time = ""
headers_post_selected_pickup_time = {'Content-type': 'application/json', 'Accept': 'application/json',
                                     'x-api-key': ''}
headers_no_apikey_post_selected_pickup_time = {'Content-type': 'application/json', 'Accept': 'application/json'}


class TicketBookingTestcases(unittest.TestCase):
    def get_list_of_food_positive_test_one(self):
        general_obj = FoodBooking()
        status_code, response_json = general_obj.get_food(url_list_of_food, {'user_id': 1, 'theater_id': 1},
                                                          headers_list_of_food)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
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
        status_code, response_json = general_obj.get_food(url_list_of_food, {'user_id': 1, 'theater_id': 1},
                                                          headers_no_apikey_list_of_food)
        print(status_code)
        self.assertEqual(status_code, 483)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Forbidden", "ERR: Failed to get the appropriate negative response")

    def post_selected_food_positive_test_one(self):
        general_obj = FoodBooking()
        status_code, response_json = general_obj.post_food(url_post_selected_food,
                                                           {'user_id': 1, 'booking_id': 1, 'food_id': 1, 'quantity': 1},
                                                           headers_post_selected_food)
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
        status_code, response_json = general_obj.post_food(url_post_selected_food, None,
                                                           headers_no_apikey_post_selected_food)
        print(status_code)
        self.assertEqual(status_code, 483)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Forbidden", "ERR: Failed to get the appropriate negative response")

    def get_list_of_pickup_times_positive_test_one(self):
        general_obj = FoodBooking()
        status_code, response_json = general_obj.get_pickup_times(url_list_of_pickup_times,
                                                                  {'user_id': 1, 'booking_id': 1},
                                                                  headers_list_of_pickup_times)
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
                                                                  headers_no_apikey_list_of_pickup_times)
        print(status_code)
        self.assertEqual(status_code, 483)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Forbidden", "ERR: Failed to get the appropriate negative response")

    def post_selected_pickup_time_positive_test_one(self):
        general_obj = FoodBooking()
        status_code, response_json = general_obj.post_pickup_times(url_post_selected_pickup_time,
                                                                   {'user_id': 1, 'booking_id': 1,
                                                                    'pickup_time': '12:00:00'},
                                                                   headers_post_selected_theater)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['pickup_time']
        self.assertEqual(str(actual_val), "12:00:00", "ERR: Failed to post the appropriate pickup time")

    def post_selected_pickup_time_negative_test_one(self):
        general_obj = FoodBooking()
        status_code, response_json = general_obj.post_pickup_times(url_post_selected_pickup_time, None,
                                                                   headers_no_apikey_post_selected_pickup_time)
        print(status_code)
        self.assertEqual(status_code, 483)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Forbidden", "ERR: Failed to get the appropriate negative response")


if __name__ == '__main__':
    unittest.main()
