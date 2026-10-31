"""Program 25: Find the maximum and minimum in a list without max() or min()."""


def find_max_min(numbers):
    """Return a tuple (maximum, minimum). Raise ValueError for an empty list."""
    if len(numbers) == 0:
        raise ValueError("List is empty")

    maximum = numbers[0]
    minimum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return (maximum, minimum)


if __name__ == "__main__":
    data = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    largest, smallest = find_max_min(data)
    print("Maximum:", largest, "Minimum:", smallest)
