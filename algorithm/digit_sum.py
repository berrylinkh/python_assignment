

def digit_sum(number):
 total_sum =0
 total = 0
 if number < 9:
  while (number!=1):
   total += number % 10
   number //=10
   while (total < 9):
    total_sum += total % 10
    total_sum //=10
 return total_sum
print(digit_sum(12345))
