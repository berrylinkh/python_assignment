# PSUEDOCODE
# START
# CREATE A REQUEST FOR THREE SCORE FROM THE USER
# ADD THE SUM OF THE SCORES TOGETHER
# CALCULATE THE AVERAGE (TOTAL SUM / THREE) 
# USE THE RESULT TO PRINT OUT THE GRADE OF THE SCORE USING THE IF EL STATEMENT.
# END


score_one = int(input("Enter score one"))
score_two = int(input("Enter score two"))
score_three = int(input("Enter score three"))

sum=0
sum = score_one +score_two + score_three
print (sum)
average = sum / 3
print (average)

if(90 <= average <= 100):
	print("The grade is A")

elif(80<= average < 90):
	print("The grade is B")

elif(70 <= average <80):
	print("The grade is C")

elif(60 <= average < 70):
	print("The grade is D")

elif(0 <= average < 60):
	print("The grade is F")


