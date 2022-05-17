__author__ = 'Sahana Pandurangi Raghavendra'
__author__ = 'Megana Reddy Boddam'

import unittest
from ticket_booking_testcase import *
def suite():
    suite = unittest.TestSuite()
    testcases = ["get_list_of_dates_positive_test_one",
             "get_list_of_dates_negative_test_one",
             "post_selected_date_positive_test_one",
             "post_selected_date_negative_test_one",
             "get_list_of_times_positive_test_one",
             "get_list_of_times_negative_test_one",
             "post_selected_time_positive_test_one",
             "post_selected_time_negative_test_one",
             "get_list_of_seats_positive_test_one",
             "get_list_of_seats_negative_test_one",
             "post_selected_seats_positive_test_one",
             "post_selected_seats_negative_test_one",
             ]
    for i in range(len(testcases)):
        suite.addTest(TicketBookingTestcases(testcases[i]))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())