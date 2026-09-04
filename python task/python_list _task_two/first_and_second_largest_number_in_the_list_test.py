
from unittest import TestCase
from first_and_second_largest_number_in_the_list import *

class FirstAndSecondLargestNumberInTheListTest(TestCase):

    def test_sort_numbers_in_ascending_order(self):
        input_numbers = [1, 5, 87, 45, 8, 8]
        actual_result = sort_numbers_in_ascending_order(input_numbers)
        expected_result = [1, 5,8,8,45,87]
        self.assertEqual(expected_result, actual_result)

    def test_get_first_and_second_largest_number(self):
        input_numbers = [1, 5, 8, 8, 45, 87]
        actual_result = get_first_and_second_largest_number(input_numbers)
        expected_result = [45, 87]
        self.assertEqual(expected_result, actual_result)
