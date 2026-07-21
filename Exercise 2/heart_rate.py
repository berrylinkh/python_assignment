user_input = int(input("enter age: "))
beat_per_minute = 220
lower_boundary = 50
upper_boundary = 50

heart_rate = int(beat_per_minute - user_input)
heart_rate_for_lower_boundary = int(heart_rate * 0.50)
heart_rate_for_upper_boundary = int(heart_rate * 0.85)

print ("heart rate: ",heart_rate )
print ("lower boundary is: ",heart_rate_for_lower_boundary)
print ("upper boundary is: ",heart_rate_for_upper_boundary)