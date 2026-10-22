"""Program 26: Calculate a list's sum without sum()."""


def sum_of_list(numbers):
    """Return the sum of all numbers; an empty list returns 0."""
    total = 0
    for num in numbers:
        total += num
    return total


if __name__ == "__main__":
    print(sum_of_list([1, 2, 3, 4]))
