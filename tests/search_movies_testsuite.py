__author__ = 'Sahana Pandurangi Raghavendra'
__author__ = 'Megana Reddy Boddam'

import unittest
from search_movies_testcases import *
def suite():
    suite = unittest.TestSuite()
    testcases = ["get_list_of_cities_positive_test_one",
             "get_list_of_cities_negative_test_one",
             "get_list_of_cities_negative_test_two",
             "get_list_of_cities_negative_test_three",
             "post_selected_city_positive_test_one",
             "post_selected_city_negative_test_one",
             "get_list_of_theaters_positive_test_one",
             "get_list_of_theaters_negative_test_one",
             "get_list_of_theaters_invalid_parameters",
             "post_selected_theater_positive_test_one",
             "post_selected_theater_negative_test_one",
             "get_list_of_movies_positive_test_one",
             "get_list_of_movies_negative_test_one",
             "post_selected_movie_positive_test_one",
             "post_selected_movie_negative_test_one"
             ]
    for i in range(len(testcases)):
        suite.addTest(SearchMoviesTestcases(testcases[i]))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())