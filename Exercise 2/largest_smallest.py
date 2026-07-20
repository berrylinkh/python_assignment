number_one =int(input('Enter first value: '))
number_two =int(input('Enter second value: '))
number_three =int(input('Enter third value: '))

if number_one > number_two and  number_one > number_three:
	print("largest: ", number_one)

if number_two > number_one and  number_two > number_three:
	print("largest: ", number_two)

if number_three > number_one and  number_three > number_two:
	print("largest: ", number_three)

if number_one < number_two and  number_one < number_three:
	print("smallest: ", number_one)

if number_two < number_one and  number_two < number_three:
	print("smallest: ", number_two)
 
if number_three < number_one and  number_three < number_two:
	print("smallest: ", number_three)