def process(items):
    total = 0
    for x in items:
        total = total + score(x)
    return total


def score(x):
    bonus = 0
    if x > 10:
        bonus = 5
    return x + bonus


data = [4, 12, 7, 20]
result = process(data)
print(result)
