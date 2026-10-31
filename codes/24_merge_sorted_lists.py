"""Program 24: Merge two already-sorted lists into one sorted list."""


def merge_sorted_lists(list1, list2):
    """Return one sorted list containing all elements of list1 and list2."""
    merged = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    # One list is finished - copy what is left in the other one.
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged


if __name__ == "__main__":
    a = [int(x) for x in input("Enter first sorted list: ").split()]
    b = [int(x) for x in input("Enter second sorted list: ").split()]
    print("Merged list:", merge_sorted_lists(a, b))
