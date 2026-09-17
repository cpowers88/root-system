# Goal: Convert camelCase into snake_case

# Given: The user enters a camelCase variable name
# Find: The same name in snake_case

# Step 1: Ask the user for camelCase text adn store it
camel = input("camelCase: ")

# Step 2: Create an empty result string for the snake_case version
result = ""

# Step 3: Loop through each characer in the camelCase text
for character in camel:
    if character.isupper():
        result = result + "_" + character.lower()
    else:
        result = result + character
print (result)


    