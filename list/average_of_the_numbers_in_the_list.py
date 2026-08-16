




lists = [7,11,3,1,6,12,4,5,8,10]
total_number = 10
def list_length_of_a_list (numbers):
    sum = 0
    for element in numbers:
        sum +=element
    average = sum / total_number
    return average

print(list_length_of_a_list(lists))
