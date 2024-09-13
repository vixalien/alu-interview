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
    if n <= 1:
        return 0
    if is_prime(n):
        return n
    else:
        prime = small_prime(n)
        if prime:
            return prime + minOperations(int(n/prime))


def is_prime(n):
    """
    Check if it's a prime number
    """
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False

    for i in range(3, floor(sqrt(n)), 2):
        if n % i == 0:
            return False
    return True


def small_prime(n):
    """
    Gets the smallest prime factor
    """
    for i in range(2, int(n/2 + 1)):
        if n % i == 0:
            return i
    return None
