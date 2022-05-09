import unittest
import traceback
import logging

class AssertionEqual(unittest.TestCase):
    @classmethod
    def assert_equal(actual_output, expected_output, msg):
        print("actual output is:")
        print(actual_output)
        print("expected output is:")
        print(expected_output)
        try:
            assert actual_output == expected_output, msg
        except AssertionError as e:
            print(traceback.format_exc(), "error")
            raise e