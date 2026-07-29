from third import bill_calculator

x = float(input("What is the total amount? "))
y = float(input("What is the tax percentage in decimal value? "))
z = float(input("What is the tip percentage in decimal value? "))

q = bill_calculator(x, y, z)
print(q)
