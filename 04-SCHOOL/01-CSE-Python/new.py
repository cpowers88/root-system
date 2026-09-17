cash = float(input("How much money do you have? "))

if cash >= 2.0:
    print("I can only buy the socks...")
elif cash >= 15.0:
    print("I can buy the shorts.")
elif cash >= 25.0:
    print("I can buy the shirt.")
elif cash >= 100.0:
    print("I can buy the jacket.")
elif cash >= 500.0:
    print("I can buy anything!")
else:
    print("I cannot buy anything...")
