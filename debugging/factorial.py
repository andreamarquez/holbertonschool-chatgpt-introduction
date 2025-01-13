#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n
    return result

if len(sys.argv) != 2:
    print("Usage: ./factorial.py <number>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
    if n < 0:
        raise ValueError("Number must be non-negative")
except ValueError as e:
    print(e)
    sys.exit(1)

f = factorial(n)
print(f)
