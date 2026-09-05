def count_above_threshold(numbers: list[int], threshold: int) -> int:
    """Counts how many values in the list are strictly greater than the threshold."""
    count = 0
    for value in numbers:
        if value > threshold:
            count += 1
    return count