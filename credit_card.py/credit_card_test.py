
from unittest import TestCase
from credit_card import * 

class credit_card_Test (TestCase):
    def test_that_count_credit_card_number(self): 
        card_input= "4388576018402626"
        actual_result = count_credit_card_number(card_input)
        expected_result =16
        self.assertEqual(actual_result, expected_result)
        
    def test_that_convert_card_number_is_converted_into_list(self):
        card_input= "4388576018402626";
        actual_result = convert_card_number_into_an_list(card_input);
        expected_result= [4,3,8,8,5,7,6,0,1,8,4,0,2,6,2,6]
        self.assertEqual(actual_result, expected_result)
            
    def test_that_credit_card_type(self):
        card_input = [4,3,8,8,5,7,6,0,1,8,4,0,2,6,2,6]
        actual_result = check_credit_card_type(card_input)
        expected_result = "MasterCard"
        self.assertEqual(actual_result, expected_result)
            
    def test_that_double_second_digit_of_the_card(self):
        card_input = [4,3,8,8,5,7,6,0,1,8,4,0,2,6,2,6]
        actual_result = double_second_digit_of_the_card(card_input)
        expected_result = [8,3,7,8,1,7,3,0,2,8,8,0,4,6,4,6]
        self.assertEqual(actual_result, expected_result)
        
    def test_that_add_all_the_numbers_after_it_has_been_doubled(self):
        card_input = [8,3,7,8,1,7,3,0,2,8,8,0,4,6,4,6]
        actual_result = add_all_the_numbers_after_it_has_been_doubled(card_input)
        expected_result = 37
        self.assertEqual(actual_result, expected_result)

        
    def test_that_add_all_the_numbers_in_odd_index(self):
        card_input = [8,3,7,8,1,7,3,0,2,8,8,0,4,6,4,6]
        actual_result = add_all_the_numbers_in_odd_index(card_input)
        expected_result = 38
        self.assertEqual(actual_result, expected_result)
            
    def test_that_add_double_and_odd_total_in_odd(self):
        card_input = [8,3,7,8,1,7,3,0,2,8,8,0,4,6,4,6]
        actual_result = add_double_and_odd_total_in_odd(card_input)
        expected_result = 75
        self.assertEqual(actual_result, expected_result)
             

    def test_that_return_credit_card_validity(self):
        card_count ="4388576018402626"
        card_input =[4,3,8,8,5,7,6,0,1,8,4,0,2,6,2,6]
        actual_result = return_credit_card_validity(card_count,card_input)
        expected_result = "Invalid"
        self.assertEqual(actual_result, expected_result)  
                     
