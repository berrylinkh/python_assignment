# PSUEDOCODE
# START
# COLLECT INPUT IN STRING
# USE LEN TO KNOW THE LENGTH OF THE STRING
# THE LENGTH OF THE STRING DETERMINES THE OUTPUT
# USE IF ELIF STATEMENT LESS THAN 5 FOR SHORT, FROM 5 TO 10 FOR MEDIUM AND 11 ABOVE FOR LONG STRING
# PRINT OUT THE RESULT OF THE STRING INPUTTED.
# END


letter = str(input("enter option: "))
length = len(letter)

if length < 5 :
	print ("short string")

elif  length >= 5 and length <= 10 :
	print ("medium string")


elif  length >10  :
	print ("long string")
