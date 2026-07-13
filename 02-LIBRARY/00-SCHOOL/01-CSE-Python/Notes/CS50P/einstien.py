# Goal: Ask the user fo mass and calculate energy using E = m * c^2
# Given: The user enters mass as  a whole number
# Find: The energy value

# Step 1: Ask the user for mass and store it
text = input("Please enter the mass in kilograms: ")
# Step 2: Convert the user's input to an integer and store it
mass = int(text)
# Step 3: Store the speed of light in a variable
c = 299792458
# Step 4: Calculate the energy using the formula E = m * c^2 and store it
energy = mass * c ** 2
# Step 5: Print the energy result
print(energy)
