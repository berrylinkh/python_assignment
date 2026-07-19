weight =int(input("Enter value : "))
height =int(input("Enter value : "))
bmi = weight / (height * height)

if weight < 18.5:
	print ("Underweight")

if weight >=18.5 and weight <= 24.9:
	print ("Normal")

if weight >=25 and weight <= 29.9:
	print ("Normal")

if weight >=30:
	print ("Obess")