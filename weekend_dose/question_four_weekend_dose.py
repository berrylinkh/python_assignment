even_number =0
odd_number =0

for number in [1,2,3,4,5,6,7,8,9,10]:
    if number % 2 == 0:
        even_number += 1

    else: 
        odd_number +=1
print(f" Total even number=  {even_number}")
print(f" Total odd number= {odd_number}")
    
