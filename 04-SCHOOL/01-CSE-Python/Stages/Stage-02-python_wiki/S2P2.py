# write a script that asks for 'score'(int) and asks"Did you attend at aleast 75% of classes?(yes/no)" as a string, then prints "pass" only if the score is 60 or above and the attendance answer was "yes". Watch out - comparing a string input to "yes" needs the exact match, so input() capitalization matters. Post the code and one run.
score = int(input("Score: "))
attendance = input("Did you attend at least '75%' of classes? (yes/no): ").lower()

if score >= 90 and attendance == "yes":
    print("A")
elif score >= 80 and attendance == "yes":
    print("B")
elif score >= 70 and attendance == "yes":
    print("C")
elif score >= 60 and attendance == "yes":
    print("D")
else:
    print("fail")
