
numbers = [1, 5, 87, 45, 8, 8]
sorted_numbers = [1, 5, 8, 8, 45, 87]

def sort_numbers_in_ascending_order(numbers):
    temp_value = 0
    for outer_index in range(0, len(numbers)):
        for inner_index in range(0, len(numbers)):
            if (numbers[outer_index] < numbers[inner_index]):
                temp_value = numbers[outer_index]
                numbers[outer_index] = numbers[inner_index]
                numbers[inner_index] = temp_value
    return numbers

print(sort_numbers_in_ascending_order(numbers))


def get_first_and_second_largest_number(sorted_numbers):
    result = []
    result.append(sorted_numbers[-2])
    result.append(sorted_numbers[-1])
    return result

print(get_first_and_second_largest_number(sorted_numbers))
