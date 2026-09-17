

from functools import reduce
def convert_list_of_string_to_integer_using_map(given):
     
    given =list(map(int,given))
    
    return given



def add_10_to_list_of_number_using_map(given_numbers):
     
    given_numbers =list(map(lambda number: number + 10, given_numbers))
    
    return given_numbers



def convert_celsisu_to_fahrenheit_using_map (given_numbers):
     
    given_numbers =list(map(lambda celsius:int (celsius *1.8 + 32), given_numbers))
    
    return given_numbers



def remove_none_from_list_using_filter (given_filter):
     
    given_filter =list(filter(lambda number:number, given_filter))
    
    return given_filter



def get_numbers_divisible_by3_from_list_using_filter (divisible_by3):
     
    divisible_by3 = list(filter(lambda number:number % 3 ==0, divisible_by3))
    
    return divisible_by3



def get_positive_numbers_in_list_using_filter (given_list):
     
    given_list = list(filter(lambda number: number > -1, given_list))

    return given_list



dictionary =[{'name':'Alice','age': 30}, {'name':'Bob', 'age': 20}]


def get_age_greater_than_25 (dictionary):
     
    dictionary = list(filter(lambda person:person['age'] >25, dictionary))
    
    return dictionary



def get_sum_of_all_numbers (given):
     
    given = reduce(lambda value_one, value_two: value_one + value_two, given)
    
    return given



def get_product_of_all_numbers (given):
     
    given = reduce(lambda value_one, value_two: value_one * value_two, given)
    
    return given



def get_maximum_number (given):
     
    given = reduce(lambda largest, number: largest if largest > number else number, given)
    
    return given



def concatenate_strings (word):
     
    word = reduce(lambda word, text: word + text, word)
    
    return word



def merge_dictionaries (merge):
     
    merge = reduce(lambda element, value: {**element, **value}, merge)
    
    return merge



def cummulative_sum_of_squares_of_all_numbers (given):
     
    given = reduce(lambda value_one, value_two: value_one*2 + value_two , given)
    
    return given

