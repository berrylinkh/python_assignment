





lists = [7,11,3,1,6,12,4,5,8,10]

def list_length_of_a_list (numbers):
    count =0    
    multiply = 1
    for number in range (2,len(lists),3):
            multiply *=lists[number]
    return multiply

print(list_length_of_a_list(lists))
