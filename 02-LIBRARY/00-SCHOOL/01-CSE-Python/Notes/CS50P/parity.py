# Goal: Determine whether a number is even or odd

# Given: The user enters a number
# Find: Whether the number is even or odd

# Step 1: Ask the user for a number, convert it to an integer, and store it
number = int(input("What's the number? "))

# Step 2: If number divided by 2 has a remainder of 0, print "even"
if number % 2 == 0:
    print("even")

# Step 3: Otherwise, print "odd"
else:
    print("odd")
