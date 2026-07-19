total_bill =int(input("Enter value : "))
is_member =str(input("Enter answer : "))


if total_bill >=1000 and is_member=="yes":
	print ("10% off")

if total_bill >=1000 and is_member=="no":
	print ("5% off")

else:
	print ("total bill = ",total_bill, "\nNo discount",)
