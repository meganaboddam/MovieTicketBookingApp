__author__ = 'Sahana Pandurangi Raghavendra'
__author__ = 'Megana Reddy Boddam'

import unittest
from search_movies_lib import *

url_list_of_cities = "https://9qhi5gewy6.execute-api.us-east-1.amazonaws.com/prod/listofcities"
url_list_of_theaters = "https://9qhi5gewy6.execute-api.us-east-1.amazonaws.com/prod/listoftheaters"
url_list_of_movies = "https://9qhi5gewy6.execute-api.us-east-1.amazonaws.com/prod/listofmovies"

headers_with_apikey = {'Content-type': 'application/json', 'Accept': 'application/json',
                       'x-api-key': 'ynbWkSO7m32Mk64vd2d7NaD6VyYm8D1fH18A01O9'}


# Testcases that test all the endpoints pertaining to search movies lambda interface.
class SearchMoviesTestcases(unittest.TestCase):
    def get_list_of_cities_positive_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_cities(url_list_of_cities, {'user_id': 1}, headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        print("Checking First City")
        actual_val = response_json['city'][0]['city_name']
        self.assertEqual(str(actual_val), "Seattle", "ERR: Failed to get the appropriate city")
        print("Checking Second City")
        actual_val = response_json['city'][1]['city_name']
        self.assertEqual(str(actual_val), "Kirkland", "ERR: Failed to get the appropriate city")
        print("Checking Third City")
        actual_val = response_json['city'][2]['city_name']
        self.assertEqual(str(actual_val), "Redmond", "ERR: Failed to get the appropriate city")

    def get_list_of_cities_negative_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_cities(url_list_of_cities, {'user_id': "abc"},
                                                            headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid User Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_cities_negative_test_two(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_cities(url_list_of_cities, {'user_id': None},
                                                            headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid User Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_cities_negative_test_three(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_cities(url_list_of_cities, {'user_id': 99999999},
                                                            headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid User Input", "ERR: Failed to get the appropriate negative response")

    def post_selected_city_positive_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.post_city(url_list_of_cities, {'user_id': 1, 'city_code': 1},
                                                           headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['city_name']
        self.assertEqual(str(actual_val), "Seattle", "ERR: Failed to post the appropriate city")

    def post_selected_city_negative_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.post_city(url_list_of_cities, {'user_id': 1, 'city_code': "abc"},
                                                           headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid User Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_theaters_positive_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_theaters(url_list_of_theaters, {'user_id': 1, 'city_code': 1},
                                                              headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        print("Checking First Theater")
        actual_val = response_json['theater'][0]['theater_name']
        self.assertEqual(str(actual_val), "Cinemark", "ERR: Failed to get the appropriate theater")
        print("Checking Second Theater")
        actual_val = response_json['theater'][1]['theater_name']
        self.assertEqual(str(actual_val), "Lincoln Memorial Theater", "ERR: Failed to get the appropriate theater")
        print("Checking Third Theater")
        actual_val = response_json['theater'][2]['theater_name']
        self.assertEqual(str(actual_val), "Regal", "ERR: Failed to get the appropriate theater")

    def get_list_of_theaters_negative_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_theaters(url_list_of_theaters, {'user_id': 1, 'city_code': "abc"},
                                                              headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid User Inputs", "ERR: Failed to get the appropriate negative response")

    def get_list_of_theaters_invalid_parameters(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_theaters(url_list_of_theaters, {'user_id': 1, 'city_code': 'AB56'},
                                                              headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid User Input", "ERR: Failed to get the appropriate negative response")

    def post_selected_theater_positive_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.post_theater(url_list_of_theaters,
                                                              {'user_id': 1, 'theater_id': 1},
                                                              headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['theater_name']
        self.assertEqual(str(actual_val), "Cinemark", "ERR: Failed to post the appropriate city")

    def post_selected_theater_negative_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.post_theater(url_list_of_theaters,
                                                              {'user_id': 1, 'theater_id': "abc"},
                                                              headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid User Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_movies_positive_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_movies(url_list_of_movies,
                                                            {'user_id': 1, 'theater_id': 1},
                                                            headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        print("Checking First Movie")
        actual_val = response_json['movie'][0]['movie_name']
        self.assertEqual(str(actual_val), "Top Gun: Maverick", "ERR: Failed to get the appropriate movie")
        print("Checking Second Movie")
        actual_val = response_json['movie'][1]['movie_name']
        self.assertEqual(str(actual_val), "Pushpa: The Rise - Part 1", "ERR: Failed to get the appropriate movie")

    def get_list_of_movies_negative_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_movies(url_list_of_movies,
                                                            {'user_id': 1, 'theater_id': 'abc'},
                                                            headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid User Inputs", "ERR: Failed to get the appropriate negative response")

    def post_selected_movie_positive_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.post_movie(url_list_of_movies,
                                                            {'user_id': 1, 'movie_id': 1},
                                                            headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['movie_name']
        self.assertEqual(str(actual_val), "Top Gun: Maverick", "ERR: Failed to post the appropriate movie")

    def post_selected_movie_negative_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.post_movie(url_list_of_movies,
                                                            {'user_id': 1, 'movie_id': 'abc'},
                                                            headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid User Inputs", "ERR: Failed to get the appropriate negative response")
