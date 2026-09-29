from unittest import TestCase
from boolean_perfect_square import *

class boolean_perfect_sqaure_test(TestCase):
    def check_perfect_square_test (self):
        given = [0,1,2,3,4,9,10,16,25,26]
        actual = check_perfect_square_and_return_boolean(given)
        expected = [True,True,False,False,True,True,False,True,True,False]
        self.assertTrue (actual, expected)
