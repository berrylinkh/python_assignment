



lists = [7,11,3,1,6,12,4,5,8,10]

def list_length_of_a_list (numbers):
    sum = 0
    for element in lists:
        if (element % 2 !=0):
            sum +=element
    return sum

print(list_length_of_a_list(lists))
