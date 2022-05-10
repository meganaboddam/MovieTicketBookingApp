__author__ = 'Sahana Pandurangi Raghavendra'
__author__ = 'Megana Reddy Boddam'

import unittest
from payment_processing_lib import *
import unittest

url_booking_cost = "https://9qhi5gewy6.execute-api.us-east-1.amazonaws.com/prod/bookingcost"
url_list_of_tickets = "https://9qhi5gewy6.execute-api.us-east-1.amazonaws.com/prod/listoftickets"

headers_with_api_key = {'Content-type': 'application/json', 'Accept': 'application/json',
                        'x-api-key': 'ynbWkSO7m32Mk64vd2d7NaD6VyYm8D1fH18A01O9'}
headers_no_apikey = {'Content-type': 'application/json', 'Accept': 'application/json'}


# Testcases that test all the endpoints pertaining to payment processing lambda interfaces.
class PaymentProcessingTestcases(unittest.TestCase):

    def post_booking_cost_positive_test_one(self):
        general_obj = PaymentProcessing()
        status_code, response_json = general_obj.post_booking_cost(url_booking_cost, {'booking_id': 1},
                                                                   headers_with_api_key)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['cost']
        self.assertEqual(str(actual_val), "20", "ERR: Failed to post the appropriate booking cost")

    def post_booking_cost_negative_test_one(self):
        general_obj = PaymentProcessing()
        status_code, response_json = general_obj.post_booking_cost(url_booking_cost, {'booking_id': 1},
                                                                   headers_no_apikey)
        print(status_code)
        self.assertEqual(status_code, 403)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Forbidden", "ERR: Failed to get the appropriate negative response")

    def get_booking_cost_positive_test_one(self):
        general_obj = PaymentProcessing()
        status_code, response_json = general_obj.get_booking_cost(url_booking_cost, {'booking_id': 1},
                                                                  headers_with_api_key)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['cost']
        self.assertEqual(str(actual_val), "20", "ERR: Failed to get the appropriate booking cost")

    def get_booking_cost_negative_test_one(self):
        general_obj = PaymentProcessing()
        status_code, response_json = general_obj.get_booking_cost(url_booking_cost, {'booking_id': 1},
                                                                  headers_no_apikey)
        print(status_code)
        self.assertEqual(status_code, 403)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Forbidden", "ERR: Failed to get the appropriate negative response")

    def get_list_of_tickets_positive_test_one(self):
        general_obj = PaymentProcessing()
        status_code, response_json = general_obj.get_tickets(url_list_of_tickets, {'booking_id': 1},
                                                             headers_with_api_key)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        self.check_ticket_positive_test_one(response_json, 0)
        self.check_ticket_positive_test_one(response_json, 1)

    def check_ticket_positive_test_one(self, response_json, index):
        print("Checking city name on ticket")
        actual_val = response_json['ticket'][index]['city_name']
        self.assertEqual(str(actual_val), "Seattle", "ERR: Failed to get the appropriate ticket")
        print("Checking theater name on ticket")
        actual_val = response_json['ticket'][index]['theater_name']
        self.assertEqual(str(actual_val), "Cinemark", "ERR: Failed to get the appropriate ticket")
        print("Checking movie on ticket")
        actual_val = response_json['ticket'][index]['movie_name']
        self.assertEqual(str(actual_val), "Top Gun: Maverick", "ERR: Failed to get the appropriate ticket")
        print("Checking date on ticket")
        actual_val = response_json['ticket'][index]['date']
        self.assertEqual(str(actual_val), "2022-06-01", "ERR: Failed to get the appropriate ticket")
        print("Checking time on ticket")
        actual_val = response_json['ticket'][index]['time']
        self.assertEqual(str(actual_val), "12:30:00", "ERR: Failed to get the appropriate ticket")
        print("Checking theater room on ticket")
        actual_val = response_json['ticket'][index]['room_name']
        self.assertEqual(str(actual_val), "A", "ERR: Failed to get the appropriate ticket")
        print("Checking seat row on ticket")
        actual_val = response_json['ticket'][index]['seat_row']
        self.assertEqual(str(actual_val), "A", "ERR: Failed to get the appropriate ticket")
        print("Checking seat number on ticket")
        actual_val = response_json['ticket'][index]['seat_number']
        self.assertEqual(str(actual_val), "1", "ERR: Failed to get the appropriate ticket")
        print("Checking food items on ticket")
        actual_val = response_json['ticket'][index]['food'][0]['food_name']
        self.assertEqual(str(actual_val), "Butter Popcorn (Small)", "ERR: Failed to get the appropriate ticket")
        print("Checking food quantity on ticket")
        actual_val = response_json['ticket'][index]['food'][0]['quantity']
        self.assertEqual(str(actual_val), "1", "ERR: Failed to get the appropriate ticket")
        print("Checking food pickup time on ticket")
        actual_val = response_json['ticket'][index]['pickup_time']
        self.assertEqual(str(actual_val), "12:00:00", "ERR: Failed to get the appropriate ticket")
        print("Checking booking cost on ticket")
        actual_val = response_json['ticket'][index]['cost']
        self.assertEqual(str(actual_val), "20", "ERR: Failed to get the appropriate ticket")

    def get_list_of_tickets_negative_test_one(self):
        general_obj = PaymentProcessing()
        status_code, response_json = general_obj.get_tickets(url_list_of_tickets, {'booking_id': 1},
                                                             headers_no_apikey)
        print(status_code)
        self.assertEqual(status_code, 403)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Forbidden", "ERR: Failed to get the appropriate negative response")
