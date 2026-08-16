

lists_number =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def construct_list_of_sequential_number(number):
    add =0
    for numbers in range (2,len(lists_number),3):
        add += lists_number[numbers]
    return add

print ( construct_list_of_sequential_number(list))
