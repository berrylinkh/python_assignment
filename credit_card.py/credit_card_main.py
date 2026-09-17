
from credit_card import *

user_card_number = input("Hello, Kindly enter your card details to verify: ")

card_conversion= convert_card_number_into_an_list(user_card_number)
  
print()
print ("Credit Card Type: "+check_credit_card_type(card_conversion))
print ("Card Number: "+user_card_number)
print ("Credit card digit length: ",count_credit_card_number(user_card_number));
print ("Credit card Status: "+return_credit_card_validity(user_card_number,card_conversion))
print()

