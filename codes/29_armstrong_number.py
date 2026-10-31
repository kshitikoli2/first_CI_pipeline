"""Program 29: Check whether a number is an Armstrong number."""


def is_armstrong(number):
    """Return True if the number equals the sum of its digits,
    each raised to the power of the number of digits (153 = 1^3 + 5^3 + 3^3).
    Negative numbers return False.
    """
    if number < 0:
        return False

    digits = str(number)
    power = len(digits)
    total = 0
    for d in digits:
        total += int(d) ** power
    return total == number


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print("Armstrong number:", is_armstrong(n))
