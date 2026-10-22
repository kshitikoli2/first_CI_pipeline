"""Program 28: Find common elements of two sets."""


def set_intersection(first, second):
    """Return the intersection of two sets."""
    result = set()
    for item in first:
        if item in second:
            result.add(item)
    return result


if __name__ == "__main__":
    print(set_intersection({1, 2, 3}, {2, 3, 4}))
