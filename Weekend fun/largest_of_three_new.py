a =int(input("Enter value : "))
b =int(input("Enter value : "))
c =int(input("Enter value : "))
largest = a

if b > largest and b > c : largest = b
if c > largest and c > b : largest = c

print("largest is: ", largest)