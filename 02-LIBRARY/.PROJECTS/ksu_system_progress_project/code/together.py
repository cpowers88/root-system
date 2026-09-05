from add_tax import add_tax

x = float(input("What is the total amount? "))
y = float(input("What is the tax percentage in decimal value? "))

v = add_tax(x, y)

print(v)
