"""Program 22: Check whether two strings are anagrams."""


def is_anagram(first, second):
    """Return True if both strings use exactly the same letters.

    - Upper/lower case is ignored.
    - Spaces are ignored.
    """
    a = first.replace(" ", "").lower()
    b = second.replace(" ", "").lower()

    if len(a) != len(b):
        return False

    # Count every character of the first string, then subtract for the second.
    counts = {}
    for ch in a:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in b:
        if counts.get(ch, 0) == 0:
            return False
        counts[ch] -= 1
    return True


if __name__ == "__main__":
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    print("Anagram:", is_anagram(s1, s2))
