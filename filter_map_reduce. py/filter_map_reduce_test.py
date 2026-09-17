
from unittest import TestCase
from filter_map_reduce import *

class fesat_your_hand (TestCase):
    
    def test_that_convert_list_of_string_to_integer_using_map (self):
        given = ["1", "2", "3", "4"]
        actual_result = convert_list_of_string_to_integer_using_map(given)
        expected_result = [1, 2, 3, 4]
        self.assertEqual(actual_result, expected_result)
        
    def test_that_add_10_to_list_of_number_using_map (self):
        given = [0, 5, 10, 15]
        actual_result = add_10_to_list_of_number_using_map(given)
        expected_result = [10, 15, 20, 25]
        self.assertEqual(actual_result, expected_result)
        
    def test_that_convert_celsisu_to_fahrenheit_using_map (self):
        given = [0, 20, 37, 100]
        actual_result = convert_celsisu_to_fahrenheit_using_map(given)
        expected_result = [32, 68, 98, 212]
        self.assertEqual(actual_result, expected_result)
        
    def test_that_remove_none_from_list_using_filter (self):
        given = [1, None, 3, None, 5]
        actual_result = remove_none_from_list_using_filter(given)
        expected_result = [1, 3, 5]
        self.assertEqual(actual_result, expected_result)
        
    def test_that_get_numbers_divisible_by3_from_list_using_filter (self):
        given = [1,3, 4, 6, 9, 12]
        actual_result = get_numbers_divisible_by3_from_list_using_filter(given)
        expected_result = [3, 6, 9, 12]
        self.assertEqual(actual_result, expected_result)
        
    def test_that_get_positive_numbers_in_list_using_filter (self):
        given = [-2, -1, 0, 1, 2]
        actual_result = get_positive_numbers_in_list_using_filter(given)
        expected_result = [0, 1, 2]
        self.assertEqual(actual_result, expected_result)
        
    def test_that_get_age_greater_than_25_in_dictionarylist_using_filter (self):
        given =dictionary = [{'name':'Alice','age': 30}, {'name':'Bob', 'age': 20}]
        actual_result = get_age_greater_than_25(given)
        expected_result = [{'name':'Alice','age': 30}]
        self.assertEqual(actual_result, expected_result)
        
    def test_that_get_sum_of_all_numbers_in_a_list (self):
        given =dictionary = [1, 2, 3, 4, 5]
        actual_result = get_sum_of_all_numbers(given)
        expected_result = 15
        self.assertEqual(actual_result, expected_result)
        
    def test_that_get_product_of_all_numbers (self):
        given =dictionary = [ 2, 3, 4]
        actual_result = get_product_of_all_numbers(given)
        expected_result = 24
        self.assertEqual(actual_result, expected_result)
        
    def test_that_get_maximum_number_in_a_list (self):
        given =dictionary = [3,7,2,9,1]
        actual_result = get_maximum_number(given)
        expected_result = 9
        self.assertEqual(actual_result, expected_result)
        
    def test_that_concatenate_strings (self):
        given =dictionary = ["Hello"," ", "World"]
        actual_result = concatenate_strings(given)
        expected_result = "Hello World"
        self.assertEqual(actual_result, expected_result)
        
    def test_that_merge_dictionaries (self):
        given =dictionary = [{'a':1}, {'b':2}, {'c':3}]
        actual_result = merge_dictionaries (given)
        expected_result = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(actual_result, expected_result)
        
    def test_that_cummulative_sum_of_squares_of_all_numbers (self):
        given =dictionary = [2,3,4] 
        actual_result =cummulative_sum_of_squares_of_all_numbers (given)
        expected_result = 18
        self.assertEqual(actual_result, expected_result)
