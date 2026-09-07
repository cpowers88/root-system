# count_above_threshold(numbers threshold)
# Takes a list of numbers
# Loops the list
# Counts how many values are strictly greater than the threshold.
# Returns that count (no Print() inside the function
# def count_t(count) -> int:
#  threshold = int(input("What is the threshold value? "))
#  num: list[int] = [10, 25, 40, 5]
#   for value in num: list[int]:
#      if value > threshold:
#     count += 1
#    return count
def count_above_threshold(numbers: list[int], threshold: int) -> int:
    """Counts how many values in the list are strictly greater than the threshold."""
    count = 0
    for value in numbers:
        if value > threshold:
            count += 1
    return count


# --- Example of how to use it ---
num = [10, 25, 40, 5]
user_threshold = int(input("What is the threshold value? "))

result = count_above_threshold(num, user_threshold)
print(f"Count above threshold: {result}")


num2 = [13, 25, 65, 98, 78, 45, 12, 35, 26, 64, 78, 5, 26]
user_threshold2 = int(input("What is the threshold value? "))

result2 = count_above_threshold(num2, user_threshold2)
print(f"Count above threshold: {result2}")
