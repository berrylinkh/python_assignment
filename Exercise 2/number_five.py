number=int(input('Enter five number: '))

digit_one = number % 10
digit_two = (number //10) % 10
digit_three=(number //100) % 10
digit_four =(number // 1000) % 10
digit_five =(number // 10000) % 10

print("number: ",digit_five , digit_four , digit_three , digit_two , digit_one)