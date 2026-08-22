# Goal: Convert :) to emoji s and :( to emoji sad
# Given: The user types a sentence
# Find: The same sentence with text faces converted into emoji

# step 1 Define a function named convert that accepts one piece of text
def convert(text):
    # step 2: Replace :) with 🙂 and store the result
    replaced_text = text.replace(":)", "🙂")
    # step 3:"" replace :( with 🙁 and store the result
    replaced_text = replaced_text.replace(":(", "🙁")
    # step 4 return the result
    return replaced_text
# step 5: Ask the user for input and store it in a variable
user_input = input("Please enter some text using :) and/or :( in it: ")
# step 6: Call the convert function using the user's input
converted_text = convert(user_input)
# step 7: Print the converted result
print(converted_text)
