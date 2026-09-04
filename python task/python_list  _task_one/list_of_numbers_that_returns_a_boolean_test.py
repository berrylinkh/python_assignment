


from unittest import TestCase
from list_of_numbers_that_returns_a_boolean_function import *
 
class TestArrayOfBooleanNumbers(TestCase):

    def test_should_return_boolean_list_for_prime_numbers(self):
        numbers = [2, 3, 4, 5]
        actual_result =  list_of_prime_numbers_of_type_boolean(numbers)
        expected_result = [True, True, False, True]

        self.assertEqual(actual_result, expected_result)


    def test_should_return_boolean_list_for_even_numbers(self):
        numbers = [2, 3, 4, 5]
        actual_result = list_of_even_numbers_of_type_boolean (numbers)
        expected_result = [True, False, True, False]

        self.assertEqual(actual_result, expected_result)

    def test_should_return_boolean_list_for_odd_numbers(self):
        numbers = [2, 3, 4, 5]
        actual_result = list_of_odd_numbers_of_type_boolean (numbers)
        expected_result = [False, True, False, True]

        self.assertEqual(actual_result, expected_result)
