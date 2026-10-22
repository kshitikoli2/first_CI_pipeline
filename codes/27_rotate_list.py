"""Program 27: Rotate a list right (or left for negative k)."""


def rotate_list(items, k):
    """Return items rotated right by k; negative k rotates left."""
    if not items:
        return []
    k = k % len(items)
    return items[-k:] + items[:-k] if k else items[:]


if __name__ == "__main__":
    print(rotate_list([1, 2, 3, 4, 5], 2))
