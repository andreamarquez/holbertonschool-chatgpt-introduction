#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer.

    Parameters:
    n (int): The integer for which the factorial is to be calculated. Must be non-negative.

    Returns:
    int: The factorial of the given integer. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the input number from the command line arguments
# Calculate the factorial and print the result
if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)
