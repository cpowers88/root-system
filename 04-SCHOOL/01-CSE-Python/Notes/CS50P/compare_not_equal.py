# Goal: Compare x and y using != 

# Given: The user enters two numbers
# Find: Whether x and y are not equal, or equal

# Step 1: Ask for x, convert it to an integer, and store it 
x = int(input("What's x? "))

# Step 2: Ask for y, convert it to an integer, and store it
y = int(input("What's y? "))

# Step 3: If x is not equal to y,
# print "x is not equal to y"
if x != y:
    print("x is not equal to y")
    
# Step 4: Otherwise, print "x is equal to y"
else:
    print("x is equal to y")