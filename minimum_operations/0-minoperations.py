#!/usr/bin/python3
"""
Minimum operation function
"""
from math import sqrt


def minOperations(n):
    """
    Get the minimum number of operations needed to get n number
    of Hs when you can only do copy and paste operations
    """
    if n <= 1:
        return 0
    if is_prime(n):
        return n
    else:
        prime = small_prime(n)
        return prime + minOperations(int(n/prime))


def is_prime(n):
    """
    Check if it's a prime number
    """
    result = True
    for i in range(2, int(sqrt(n) + 1)):
        if n % 2 == 0:
            result = False
    return result


def small_prime(n):
    """
    Gets the smallest prime factor
    """
    for i in range(2, int(n/2 + 1)):
        if n % i == 0:
            return i
    return None
