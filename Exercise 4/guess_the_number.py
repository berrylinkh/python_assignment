
real_number = 999

def guess_a_number(guess_number):

    real_number = 999

    return real_number

while (True):
    
    guess_the_number = input("Enter a random number: ")

    if  int(guess_the_number) == real_number:
            print ("Congratulation, you pass")
            break
    elif  int(guess_the_number) > real_number:
            print ("number too high, try again")
    elif  int(guess_the_number) < real_number:
            print ("number too low, try again")
    else: 
        print (input("Enter a random number: "))



