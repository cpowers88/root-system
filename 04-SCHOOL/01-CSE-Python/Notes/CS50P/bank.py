# Goal: Decide bank payout based on the user's greeting

# Given: The user enters a greeting
# Find: How much money to output

# Step 1: Ask the user for a greeting, clean it, and store it
greeting = input("Give me your best greeting please. ").strip().lower()

# Step 2: If the greeting starts with "hello", print "$0"
if greeting.startswith("hello"):
    print("$0")

# Step 3: else if the greeting starts with "h", print "$20"
elif greeting.startswith("h"):
    print("$20")

# Step 4: Otherwise, print "$100"
else:
    print("$100")



