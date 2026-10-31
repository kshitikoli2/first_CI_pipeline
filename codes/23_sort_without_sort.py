"""Program 23: Sort a list without using sort() or sorted() (Bubble Sort)."""


def bubble_sort(numbers):
    """Return a NEW list in ascending order. The original list is not changed."""
    result = list(numbers)  # copy, so the original stays the same
    n = len(result)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:  # already sorted - stop early
            break
    return result


if __name__ == "__main__":
    data = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    print("Sorted list:", bubble_sort(data))
