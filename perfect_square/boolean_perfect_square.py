

def check_perfect_square_and_return_boolean(given):
    counter = []
    for number in given:
        for count in range ( number +1):       
            if count * count == number:
                counter.append(True)
                break
            else: 
                 counter.append(False)
        return counter  
   
given = [0,1,2,3,4,9,10,16,25,26]
      
print(check_perfect_square_and_return_boolean(given))    
