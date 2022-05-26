__author__ = 'Sahana Pandurangi Raghavendra', 'Megana Reddy Boddam'

import unittest
from food_booking_testcase import *


# Test suite that
def suite():
    suite = unittest.TestSuite()
    testcases = [
        "get_list_of_food_positive_test_one",
        "get_list_of_food_negative_test_one",
        "post_selected_food_positive_test_one",
        "post_selected_food_negative_test_one",
        "get_list_of_pickup_times_positive_test_one",
        "get_list_of_pickup_times_negative_test_one",
        "post_selected_pickup_time_positive_test_one",
        "post_selected_pickup_time_negative_test_one"
    ]
    for i in range(len(testcases)):
        suite.addTest(FoodBookingTestcases(testcases[i]))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
