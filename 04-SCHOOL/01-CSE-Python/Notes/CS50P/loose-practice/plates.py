def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # check length first
    if len(s) < 2 or len(s) > 6:
        return False
    # check first two characters
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    # check numbers rule
    for c in s:
       if not c.isalpha() and not c.isdigit():
           return False
    # check punctuation rule
    number_started = False
    for c in s:
        if c .isdigit():
            number_started = True
        elif number_started:
            return False


    return True


main()