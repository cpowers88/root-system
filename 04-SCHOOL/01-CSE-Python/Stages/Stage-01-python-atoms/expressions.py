item_name = input("Item name: ")
item_price = float(input("Item price: "))
amount = int(input("How many: "))
subtotal = item_price * amount
tax_rate = float(.0825)
total = subtotal * (1 + tax_rate)
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax total: ${subtotal * tax_rate:.2f}")
print(f"Total: ${total:.2f}")