#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the input integer n. Returns 1 if n is 0.
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