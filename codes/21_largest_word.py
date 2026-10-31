"""Program 21: Find the largest (longest) word in a sentence."""

import string


def largest_word(sentence):
    """Return the longest word in the sentence.

    - Punctuation around words is ignored.
    - If two words have the same length, the first one wins.
    - If the sentence has no words, an empty string is returned.
    """
    largest = ""
    for word in sentence.split():
        clean = word.strip(string.punctuation)  # remove . , ! ? etc.
        if len(clean) > len(largest):
            largest = clean
    return largest


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print("Largest word:", largest_word(text))
