# PSUEDOCODE
# START
# COLLECT INPUT IN  NUMBER FROM THE USER
# CREATE A CONDITION TO CHECK IF THE NUMBER IS DIVISIBLE BY 3 AND 5
# PRINT OUT THE RESULT THAT IS DIVISIBLE ELSE NOT DIVISIBLE.
# END


number = int(input("Enter number: "))
if number % 3 ==0 and number % 5 ==0:
	print("It is divisible by 3 and 5")
else: print ("it is not divisible by 3 and 5")