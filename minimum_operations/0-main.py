#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

for n in (21, 19170307, 972, 1, 0, -12, 268435461):
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
