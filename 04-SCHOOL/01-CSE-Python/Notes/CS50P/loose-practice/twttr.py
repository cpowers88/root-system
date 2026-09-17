# Goal: Remove vowels from user input

# Given: The user enters some text
# Find: The same text with vowels removed

# Step 1: Ask the user for text and store it
text = input("Text please: ")

# Step 2: Create an empty result string
result = ""

# Step 3: Loop through each character in the text
for character in text:
    if character not in "aeiouAEIOU":
        result = result + character
print(result)
