import unittest
from ticket_booking_lib import *
import unittest

url_list_of_dates = ""
headers_list_of_dates = {'Content-type': 'application/json', 'Accept': 'application/json',
                         'x-api-key': ''}
headers_no_apikey_list_of_dates = {'Content-type': 'application/json', 'Accept': 'application/json'}

url_post_selected_date = ""
headers_post_selected_date = {'Content-type': 'application/json', 'Accept': 'application/json',
                              'x-api-key': ''}
headers_no_apikey_post_selected_date = {'Content-type': 'application/json', 'Accept': 'application/json'}

url_list_of_times = ""
headers_list_of_times = {'Content-type': 'application/json', 'Accept': 'application/json',
                         'x-api-key': ''}
headers_no_apikey_list_of_times = {'Content-type': 'application/json', 'Accept': 'application/json'}

url_post_selected_time = ""
headers_post_selected_time = {'Content-type': 'application/json', 'Accept': 'application/json',
                              'x-api-key': ''}
headers_no_apikey_post_selected_time = {'Content-type': 'application/json', 'Accept': 'application/json'}

url_list_of_seats = ""
headers_list_of_seats = {'Content-type': 'application/json', 'Accept': 'application/json',
                         'x-api-key': ''}
headers_no_apikey_list_of_seats = {'Content-type': 'application/json', 'Accept': 'application/json'}

url_post_selected_seat = ""
headers_post_selected_seat = {'Content-type': 'application/json', 'Accept': 'application/json',
                              'x-api-key': ''}
headers_no_apikey_post_selected_seat = {'Content-type': 'application/json', 'Accept': 'application/json'}


class TicketBookingTestcases(unittest.TestCase):
    def get_list_of_dates_positive_test_one(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.get_dates(url_list_of_dates, {'user_id': 1, 'movie_id': 1},
                                                           headers_list_of_dates)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        print("Checking First Date")
        actual_val = response_json[0]['date']
        self.assertEqual(str(actual_val), '2022-06-01', "ERR: Failed to get the appropriate date")
        print("Checking Second Date")
        actual_val = response_json[1]['date']
        self.assertEqual(str(actual_val), "2022-06-02", "ERR: Failed to get the appropriate date")
        print("Checking Third Date")
        actual_val = response_json[2]['date']
        self.assertEqual(str(actual_val), "2022-06-03", "ERR: Failed to get the appropriate date")

    def get_list_of_dates_negative_test_one(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.get_dates(url_list_of_dates, {'user_id': 1, 'movie_id': 1},
                                                           headers_no_apikey_list_of_dates)
        print(status_code)
        self.assertEqual(status_code, 483)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Forbidden", "ERR: Failed to get the appropriate negative response")

    def post_selected_date_positive_test_one(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.post_date(url_post_selected_date,
                                                           {'user_id': 1, 'movie_id': 1, 'date': '2022-06-01'},
                                                           headers_post_selected_date)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['date']
        self.assertEqual(str(actual_val), "2022-06-01", "ERR: Failed to post the appropriate date")

    def post_selected_date_negative_test_one(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.post_date(url_post_selected_date, None,
                                                           headers_no_apikey_post_selected_date)
        print(status_code)
        self.assertEqual(status_code, 483)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Forbidden", "ERR: Failed to get the appropriate negative response")

    def get_list_of_times_positive_test_one(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.get_times(url_list_of_times,
                                                           {'user_id': 1, 'movie_id': 1, 'date': '2022-06-01'},
                                                           headers_list_of_times)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        print("Checking First Time")
        actual_val = response_json[0]['time']
        self.assertEqual(str(actual_val), "12:30:00", "ERR: Failed to get the appropriate time")
        print("Checking Second Time")
        actual_val = response_json[1]['time']
        self.assertEqual(str(actual_val), "15:45:00", "ERR: Failed to get the appropriate time")
        print("Checking Third Time")
        actual_val = response_json[2]['time']
        self.assertEqual(str(actual_val), "20:00:00", "ERR: Failed to get the appropriate time")

    def get_list_of_times_negative_test_one(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.get_times(url_list_of_times, None, headers_no_apikey_list_of_times)
        print(status_code)
        self.assertEqual(status_code, 483)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Forbidden", "ERR: Failed to get the appropriate negative response")

    def post_selected_time_positive_test_one(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.post_time(url_post_selected_time,
                                                           {'user_id': 1, 'movie_id': 1,
                                                            'date': '2022-06-01', 'time': '12:30:00'},
                                                           headers_post_selected_time)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        print("Checking selected time")
        actual_val = response_json['time']
        self.assertEqual(str(actual_val), "12:30:00", "ERR: Failed to post the appropriate show time")
        print("Checking selected show id")
        actual_val = response_json['show_id']
        self.assertEqual(str(actual_val), "2", "ERR: Failed to post the appropriate show id")

    def post_selected_time_negative_test_one(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.post_time(url_post_selected_time, None,
                                                           headers_no_apikey_post_selected_time)
        print(status_code)
        self.assertEqual(status_code, 483)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Forbidden", "ERR: Failed to get the appropriate negative response")

    def get_list_of_seats_positive_test_one(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.get_seats(url_list_of_seats,
                                                           {'user_id': 1, 'show_id': 1},
                                                           headers_list_of_seats)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        print("Checking First Seat")
        actual_val = response_json['seat'][0]['seat_row']
        self.assertEqual(str(actual_val), "A", "ERR: Failed to get the appropriate seat row")
        actual_val = response_json['seat'][0]['seat_number']
        self.assertEqual(str(actual_val), "1", "ERR: Failed to get the appropriate seat number")
        print("Checking Second Seat")
        actual_val = response_json['seat'][1]['seat_row']
        self.assertEqual(str(actual_val), "D", "ERR: Failed to get the appropriate seat row")
        actual_val = response_json['seat'][1]['seat_number']
        self.assertEqual(str(actual_val), "3", "ERR: Failed to get the appropriate seat number")

    def get_list_of_seats_negative_test_one(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.get_seats(url_list_of_seats,
                                                           {'user_id': 1, 'show_id': 1},
                                                           headers_no_apikey_list_of_seats)
        print(status_code)
        self.assertEqual(status_code, 483)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Forbidden", "ERR: Failed to get the appropriate negative response")

    def post_selected_seats_positive_test_one(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.post_seats(url_post_selected_seat,
                                                            {'user_id': 1, 'seat_id': 1},
                                                            headers_post_selected_seat)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['booking_id']
        self.assertEqual(str(actual_val), "1", "ERR: Failed to post the appropriate seats")

    def post_selected_seats_negative_test_one(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.post_seats(url_post_selected_seat,
                                                            {'user_id': 1, 'seat_id': 1},
                                                            headers_no_apikey_post_selected_seat)
        print(status_code)
        self.assertEqual(status_code, 483)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Forbidden", "ERR: Failed to get the appropriate negative response")


if __name__ == '__main__':
    unittest.main()
