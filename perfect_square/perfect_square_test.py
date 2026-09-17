
from unittest import TestCase
from perfect_square import *

class perfect_square_test (TestCase):
    def perfect_square_thet_return_a_boolean_test(self):
        given = [4, 9, 25, 49]
        actual_result = check_if_it_is_a_perfect_number_and_return_boolean(given)
        expected_result = [True, True, True, True]
        self.assertTrue(actual_result,expected_result)
        
    def palindrome_thet_return_a_boolean_test(self):
        given = ["madam", "hello", "noon", "racecar"]
        actual_result = check_if_it_is_a_palindrome_and_return_boolean(given)
        expected_result = [True, False, True, True]
        self.assertTrue(actual_result,expected_result)
        
    def reverse_thet_return_a_boolean_test(self):
        given = "abcdefgh"
        actual_result = reverse_word_in_360_and_return_text(given)
        expected_result = "dcbahgfed"
        self.assertTrue(actual_result,expected_result)
        
