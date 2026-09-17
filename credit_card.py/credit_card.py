card_number = []

def count_credit_card_number(card_input):
    counter = 0

    for count in card_input:
        counter += 1

    return counter

def convert_card_number_into_an_list(card_input):

    for number in card_input:
        card_number.append(int(number))

    return card_number

def check_credit_card_type(card_input):
    if card_input[0] == 4:
        return "MasterCard"
        
    elif card_input[0] == 5:
        return "Visa Card"
        
    elif card_input[0] == 3 and card_input[1] == 7:
        return "American express Card"
        
    elif card_input[0] == 6:
        return "Discover Card"
    else:
        return "Invalid Card"

def double_second_digit_of_the_card(card_input):

    for number in range(len(card_input) - 2, -1, -2):
        double_number = card_input[number] * 2

        if double_number > 9:
            double_number = (double_number // 10) + (double_number % 10)

        card_input[number] = double_number

    return card_input

def add_all_the_numbers_after_it_has_been_doubled(card_input):
    sum_of_double_number= 0
    for number in range(len(card_input) - 2, -1, -2):
        sum_of_double_number += card_input[number]

    return sum_of_double_number

def add_all_the_numbers_in_odd_index(card_input):
    sum_of_odd_number=0
    for number in range(len(card_input) - 1, -1, -2):
        sum_of_odd_number += card_input[number]

    return sum_of_odd_number

def add_double_and_odd_total_in_odd(card_input):
    total_result =0
    total_result = add_all_the_numbers_after_it_has_been_doubled(card_input) + add_all_the_numbers_in_odd_index(card_input)
   

    return total_result

def return_credit_card_validity (card_count,card_input):
    card_counter = count_credit_card_number(card_count)
    card_digit_sum = add_double_and_odd_total_in_odd(card_input)

    if (card_count == 13 or card_count == 16) and card_digit_sum % 10 == 0:
        return "Valid"
    else:
        return "Invalid"

