

lists = [7,11,3,1,6,12,4,5,8,10]


def list_length_of_a_list (numbers):
    smallest = lists[0]
      
    for number in range (0,len(lists)):
        if smallest > lists[number]:
            smallest = lists[number]
  
    return smallest

print(list_length_of_a_list(lists))
