# Ask the user for their name (text ▬ no conversion needed)
name = input("Name: ")
# Ask the user for their age (convert to 'int')
age = int(input("Age: "))
# Ask the user for the price of something they want to buy (convert to 'float')
price = float(input("What is the price of something you would like to purchase? "))
tax_rate = float(input("Tax rate as decimal: "))
# Print a sentence using all three, including a calcultion (eg. "In 5 years, [name] will be [age + 5] years old, and the item will probably cost more than $[price].")
print(f"In 5 years, {name} will be {age + 5} years old, and the item will cost ${price * (1 + tax_rate)}.")

# Proved:
# - input() returns text
# - int() converts text to a whole number
# - float() converts text to a decimal number
# - f-strings combine text, variables, and calculations cleanly
# - round(value, 2) formats money-like output