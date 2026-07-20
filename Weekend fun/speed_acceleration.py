# PSUEDOCODE
# START
# ENTER AN INPUT FOR SPEED AT 60 METERS/SECEOND
# ENTER AN INPUT FOR ACCELERATION AT 3.5 METERS/SECEOND
# CALCULAE THE LENGTH USING (SPEED * SPEED) / 2 * ACCELERATION
# ANSWER SHOULD BE 514.286
# PRINT OUT THE RESULT.
# END

speed = int(input("Enter v: "))
acceleration = float(input("Enter a: "))

length = (speed * speed) / (2*acceleration)
print("length = ", length)