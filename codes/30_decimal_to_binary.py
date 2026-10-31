"""Program 30: Convert a decimal number to binary without using bin()."""


def decimal_to_binary(number):
    """Return the binary digits of number as a string.

    - 0 returns "0".
    - A negative number raises ValueError.
    """
    if number < 0:
        raise ValueError("Negative numbers are not supported")
    if number == 0:
        return "0"

    binary = ""
    while number > 0:
        binary = str(number % 2) + binary  # remainder is the next digit (from the right)
        number = number // 2
    return binary


if __name__ == "__main__":
    n = int(input("Enter a decimal number: "))
    print("Binary:", decimal_to_binary(n))
