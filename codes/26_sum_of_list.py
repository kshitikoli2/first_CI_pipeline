"""Program 26: Find the sum of elements in a list without using sum()."""


def sum_of_list(numbers):
    """Return the total of all numbers. An empty list gives 0."""
    total = 0
    for num in numbers:
        total += num
    return total


if __name__ == "__main__":
    data = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
    print("Sum:", sum_of_list(data))
