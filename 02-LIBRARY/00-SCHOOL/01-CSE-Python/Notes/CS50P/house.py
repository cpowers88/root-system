# Goal: Print a Hogwarts house based on a student's name

# Given: The user enters a name
# Find: The matching house

# Step 1: Ask the user for a name and store it
name = input("What's your name? ")

# Step 2: Match against the name
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
