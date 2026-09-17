def fahrenheit_to_celsius(f):
    # define name of the function and the parameter accepted in (f)

    c = float(float(f - 32) * 5) / 9

    # takes fahrenheit value when called and changes to celsius
    return c  # returns value to the call


print(f"{fahrenheit_to_celsius(98.5):.2f}")
