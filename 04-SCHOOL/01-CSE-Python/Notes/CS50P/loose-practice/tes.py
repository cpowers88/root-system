number_started = False

for character in "CS50":
    if character.isdigit():
        number_started = True
        print("Number found:", character)

print(number_started)
