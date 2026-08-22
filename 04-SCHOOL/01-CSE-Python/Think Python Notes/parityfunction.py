# Goal: Use a function to check whether a number is even

# Given: The user enter a number
# Find: Whether the number is even or odd

# Step 1: Define a function named is_even that accepts one number
def is_even(number):
 return number % 2 == 0
# Step 4: Ask the user for x, convert it to an integer, and store it
x = int(input("What's the number? "))

# Step 5: If is_even(x) returns True, print "even"
if is_even(x):
    print("even")

# Step 6: Otherwise, print "odd"
else:
    print("odd")

