# "If it's raining and I don't have an umbrella, stay inside. If it's raining and I do have an umbrella, go out with the umbrella. Otherwise, just go out."

# "A movie ticket costs $12. If you're under 13 or over 65, it costs $8 instead."

# "Grade the score: 90+ is A, 80-89 is B, 70-79 is C, below 70 is F." — you've basically already written this one in S2P1.py, so that one's free.

# Use input() for values, comparisons plus and/or where the rule needs combined conditions, elif where outcomes are mutually exclusive, else where there's a clear "otherwise." Test each with at least two different inputs so you actually see different branches fire, not just the first one you happen to type.

# One rule I want you to think about before coding it: for rule 1, what happens if you write it as three separate if statements instead of if/elif/else? Try both versions of just that one and tell me what's different in the output — that's the drill's own self-check, and it's the real reason elif exists instead of just stacking ifs.

raining = input("Is it raining? (yes/not): ").lower()
umbrella = input("DO you have an umbrella? (yes/no): ").lower()

if raining == "yes" and umbrella == "yes":
    print("Go out with the umbrella.")
elif raining == "yes" and umbrella == "no":
    print("Stay inside.")
else:
    print("Just go out.")

ticket_price = 12
age = int(input("What is your age? "))
if age < 13 or age > 65:
    ticket_price = 8
print(f"The movie ticket costs ${ticket_price}.")

score = int(input("Score: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
