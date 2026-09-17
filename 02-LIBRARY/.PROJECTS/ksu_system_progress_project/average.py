def average(numbers):

    while numbers:
        return sum(numbers) / len(numbers)


def average1(nd):
    n = 0
    rt = 0
    while nd:
        n = n + nd
        rt += 1
    return n / rt


print(average1([6, 9, 7, 4, 3]))
