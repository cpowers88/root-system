# Goal: Simulate a coke machine that accepts coins until 50 cents is paid

# Given: Coke costs 50 cents
# Find: Amount due until paid, then change owed

# Step 1: Store the total amount due
total = 50

# Step 2: While amount due is greater than 0
while total > 0:
    print("Amount Due:", total)
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        total = total - coin
print("Change Owed:", abs(total))



   