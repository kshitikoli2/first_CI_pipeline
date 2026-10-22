"""Program 22: Check whether two strings are anagrams."""


def is_anagram(first, second):
    """Return True if strings are anagrams, ignoring case and spaces."""
    first = first.replace(" ", "").lower()
    second = second.replace(" ", "").lower()
    return sorted(first) == sorted(second)


if __name__ == "__main__":
    print(is_anagram("Listen", "Silent"))
