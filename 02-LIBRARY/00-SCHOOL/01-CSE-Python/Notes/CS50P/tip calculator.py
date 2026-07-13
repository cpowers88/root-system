# Goal: Calculate a tip amount from a meal cost and tip percentage
# Given: The meal cost and the tip percentage 
# Find: The dollar amount of the tip

# Step 1: Ask the user for the meal cost and store it
meal_cost = input("What is the cost of the meal? ")
# Step 2: Remove the dollar sign and convert the meal cost to a float
meal_cost = meal_cost.replace("$", "")
meal_cost = float(meal_cost)
# Step 3: Ask the user for the tip percentage and store it
tip_percentage = input("What percentage would you like to tip? ")
# Step 4: Remove the percent sign and convert the tip percentage to a float
tip_percentage = tip_percentage.replace("%", "")
tip_percentage = float(tip_percentage) / 100
# Step 5: Calculate the tip amount by multiplying the meal cost by the tip percentage
tip_amount = meal_cost * tip_percentage
# Step 6: Print the tip amount
print(f"The tip amount is: ${tip_amount:.2f}")