# PSUEDOCODE
# START
# ENTER AN INPUT FOR DRIVING DISTANCE AT 900.5
# ENTER AN INPUT FOR MILE PER GALLON AT 25.5
# ENTER AN INPUT FOR PRICE PER GALLON AT 3.55
# CALCULAE THE LENGTH USING (DRIVING DISTANCE / MILE PER GALLON) / PRICE PER GALLON
# ANSWER SHOULD BE 125.36
# PRINT OUT THE RESULT.
# END

driving_distance = float(input("Enter driving distance : "))
mile_per_gallon = float(input("Enter mile per gallon: "))
price_per_gallon = float(input("Enter price per gallon: "))

cost_of_driving = (driving_distance / mile_per_gallon) *price_per_gallon
print("cost of driving = ", cost_of_driving)