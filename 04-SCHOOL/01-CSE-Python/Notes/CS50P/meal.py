# Goal: Convert a time string into decimal hours and print the meal time

# Given: The user enters a time like "7:30" or "12:45"
# Find: Whether it is breakfast, lunch, dinner, or none

# Step 1: Define a function named convert that accepts a time string
def convert(time):
    hour, minute = time.strip().split(':')
    hour = float(hour)
    minute = float(minute)
    minute = minute / 60
    return hour + minute
time = input("What time is it? ")
converted_time = convert(time)
if 7 <= converted_time <= 8:
    print("breakfast time")
elif 12 <= converted_time <= 13:
    print("lunch time")
elif 18 <= converted_time <= 19:
    print("dinner time")
else:
    print("none")
    

