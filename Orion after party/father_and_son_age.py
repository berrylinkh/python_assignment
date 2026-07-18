
# PSUEDOCODE
# START
# CREATE A REQUEST FOR TWO AGE INPUT FOR THE FATHER AND THE SON
# TO GET KNOW IF THE FATHER AGE IS TWICE THE SON OR NOT:
# MULTIPLY THE SON AGE BY TWO
# USE THE SON AGE TO DIVIDE THE FATHER AGE 
# USE THE RESULT TO PRINT OUT THE RESULT, THE  RESULT IS THE YEAR(S) THE FATHER AGE WILL BE TWICE THE SON.
# END

father_age = int(input("Enter the age: "))

son_age = int(input("Enter the age: "))

double_the_year = (2* son_age) - father_age
print ("the father's age will be in", double_the_year," years")
