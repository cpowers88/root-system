# Goal: Convert a numveric score into a letter grade using a cleaner decison ladder

# Given: The user enters a score
# Find: The letter grade

# Step 1: Ask the user for a score, convert it to an integer, and store it
score = int(input("What's the score? "))

# Step 2: If score is greater than or equal to 90, print "Grade: A"
if score >= 90:
    print("Grade: A")

# Step 3: Else if score is greater than or equal to 80, print "Grade: B"
elif score >= 80:
    print("Grade: B")

# Step 4: Else if score is greater than or equal to 70, print "Grade: C"
elif score >= 70:
    print("Grade: C")

# Step 5: Else if score is greater than or equal to 60, print "Grade: D"
elif score >= 60:
    print("Grade: D")

# Step 6: Otherwise, print "Grade: F"
else:
    print("Grade: F")