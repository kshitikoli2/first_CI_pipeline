"""Program 28: Find the intersection of two sets."""


def set_intersection(first, second):
    """Return a set with only the elements present in both sets."""
    common = set()
    for item in first:
        if item in second:
            common.add(item)
    return common


if __name__ == "__main__":
    a = set(input("Enter elements of first set: ").split())
    b = set(input("Enter elements of second set: ").split())
    print("Intersection:", set_intersection(a, b))
