#!/usr/bin/python3
"""
Minimum operation function
"""
from math import sqrt, floor


def minOperations(n):
    """
    Get the minimum number of operations needed to get n number
    of Hs when you can only do copy and paste operations
    """
    # If n is 1 or less, no operations are needed
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    # Continue until the factor's square is greater than n
    while factor * factor <= n:
        # While n is divisible by the current factor
        while n % factor == 0:
            # Add the factor to the operation count
            operations += factor
            # Divide n by the factor
            n //= factor
        # Move to the next potential factor
        factor += 1

    # If n is still greater than 1, it's a prime factor itself
    if n > 1:
        operations += n

    return operations
