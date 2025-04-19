#!/usr/bin/python3
"""
This function calculates the fewest number of operations
(only Copy All and Paste) to get exactly n 'H' characters.
"""


def minOperations(n):
    steps = 0
    i = 2
    while n > 1:
        if n % i == 0:
            steps += i
            n = n // i
        else:
            i += 1
    return steps
