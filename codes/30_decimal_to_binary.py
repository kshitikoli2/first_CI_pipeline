"""Program 30: Convert a non-negative decimal integer to binary."""


def decimal_to_binary(number):
    """Return the binary representation without using bin()."""
    if number < 0:
        raise ValueError("Negative numbers are not allowed")
    if number == 0:
        return "0"

    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    return binary


if __name__ == "__main__":
    print(decimal_to_binary(10))
