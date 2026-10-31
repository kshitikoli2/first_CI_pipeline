"""Program 27: Rotate a list to the right by k positions."""


def rotate_list(items, k):
    """Return a NEW list rotated right by k positions.

    - k larger than the list length wraps around.
    - A negative k rotates to the left.
    - An empty list returns [].
    """
    n = len(items)
    if n == 0:
        return []
    k = k % n  # Python's % also turns a negative k into the matching right shift
    return items[n - k:] + items[:n - k]


if __name__ == "__main__":
    data = input("Enter items separated by spaces: ").split()
    steps = int(input("Rotate by k = "))
    print("Rotated list:", rotate_list(data, steps))
