# Goal: Interpret a simple math expression and print the result

# Given: The user enters anexpression like "1+1"
# Find: The calculated result

# Step 1: Ask the user for an expression and store it
math = (input("Give me a math expression please. "))

# Step 2: Split the expression into three parts: x, operator, z
x, operator, z = math.split(" ")

# Step 3: Convert x and z into floats
x = float(x)
z = float(z)

# Step 4: Compute and print the result
if operator == "+":
    result = x + z
elif operator == "-":
    result = x - z
elif operator == "*":
    result = x * z
elif operator == "/":
    result = x / z
else:
    raise ValueError("Invalid operator")

print(result)
