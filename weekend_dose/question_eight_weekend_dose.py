number = input('Enter integer: ')

descending_order = 0
reversed_number = 0

for digit in number: 
    if digit > descending_order: 
     descending_number = int(digit)
     for value in descending_order:
        if value > reversed_number:
            reversed_number=value
print(f"The reversed  number = {reversed_number}")
