number = 1
while number < 6:
    print(number)
    number += 1
for number in range(2, 10, 2):  # 2, 4, 6, 8
    print(number)
total = 0
for number in range(1, 11):
    total += number  # same as total = total + number
print(total)  # 55
