





lists = [7,11,3,1,6,12,4,5,8,10]


def list_length_of_a_list (numbers):
    largest = lists[0]
      
    for number in range (0,len(lists)):
        if largest < lists[number]:
            largest = lists[number]
  
    return largest

print(list_length_of_a_list(lists))
