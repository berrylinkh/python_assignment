# PSUEDOCODE
# START
# COLLECT INPUT IN AGE FROM THE USER
# USE IF ELIF STATEMENT TO CONDITION IF THE INPUT IS A CHILD OR TEEN OR ADULT'
# PRINT OUT THE RESULT AND TELL THE USER WHERE THE AGE BELONG.
# END


age = int(input("enter option: "))

if age >= 0 and age <= 12: print ("Child")
elif age >12 and age <= 18: print("Teen")
elif age >18: print("Adult")