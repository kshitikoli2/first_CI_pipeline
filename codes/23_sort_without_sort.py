"""Program 23: Sort numbers without sort() or sorted()."""


def bubble_sort(numbers):
    """Return a sorted copy of numbers using bubble sort."""
    result = numbers[:]
    for i in range(len(result)):
        for j in range(len(result) - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


if __name__ == "__main__":
    print(bubble_sort([5, 2, 9, 1]))
