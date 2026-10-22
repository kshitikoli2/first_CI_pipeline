"""Program 25: Find maximum and minimum without max()/min()."""


def find_max_min(numbers):
    """Return (maximum, minimum); raise ValueError for an empty list."""
    if not numbers:
        raise ValueError("List cannot be empty")

    maximum = minimum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return maximum, minimum


if __name__ == "__main__":
    print(find_max_min([4, 9, 1, 7]))
