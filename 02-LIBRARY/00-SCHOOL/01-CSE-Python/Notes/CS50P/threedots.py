# Goal: Ask the user for text and replace spaces with three dots
# Given: The user types a sentence
# Find : The same sentence, but spaces become ...

# Step 1: Ask the user for text and store it in a variable
text = input("Can I have some text please? ")

# Step 2: Replace each space with three dots and store the result
modified_text = text.replace(" ", "...")

# Step 3: Print the changed text
print(modified_text)