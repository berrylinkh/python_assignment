

def seconds_since_midnight(hour, minute, seconds):
    hour_in_seconds = hour * 3600
    minute_in_seconds = minute * 60
    total_score = hour_in_seconds + minute_in_seconds + seconds
    
    return total_score
print(seconds_since_midnight(13,30,45))
