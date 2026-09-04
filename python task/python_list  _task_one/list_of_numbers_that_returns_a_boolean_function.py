
counter =0 ;


def list_of_prime_numbers_of_type_boolean(numbers):
    is_prime_list = []
    for index in range(0, len(numbers)):
        divisor_count = 0
        for divisor in range(1, numbers[index] + 1):
            if numbers[index] % divisor == 0:
                divisor_count += 1
        if divisor_count == 2:
            is_prime_list.append(True)
        else:
            is_prime_list.append(False)

    return is_prime_list

print(list_of_prime_numbers_of_type_boolean([2,3,4,5])) 


def list_of_even_numbers_of_type_boolean(numbers):
    is_even_list = []
    for index in range(0, len(numbers)):
        if numbers[index] % 2 == 0:
            is_even_list.append(True)
        else:
            is_even_list.append(False)

    return is_even_list

print(list_of_even_numbers_of_type_boolean([2,3,4,5]))  


def list_of_odd_numbers_of_type_boolean(numbers):
    is_odd_list = []
    for index in range(0, len(numbers)):
        if numbers[index] % 2 != 0:
            is_odd_list.append(True)
        else:
            is_odd_list.append(False)

    return is_odd_list

print(list_of_odd_numbers_of_type_boolean([2,3,4,5])) 


