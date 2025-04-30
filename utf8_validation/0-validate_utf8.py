#!/usr/bin/python3
"""
Module for UTF-8 validation.
This module defines a function to check whether a list of integers
represents a valid UTF-8 encoded sequence.
"""

def validUTF8(data):
    """
    Checks if a list of integers represents a valid UTF-8 encoding.
    """
    expected_bytes = 0

    for number in data:
        number = number & 0xFF  # Only consider the last 8 bits
        binary = bin(number)[2:].zfill(8)

        if expected_bytes == 0:
            if binary.startswith('0'):
                continue
            elif binary.startswith('110'):
                expected_bytes = 1
            elif binary.startswith('1110'):
                expected_bytes = 2
            elif binary.startswith('11110'):
                expected_bytes = 3
            else:
                return False
        else:
            if not binary.startswith('10'):
                return False
            expected_bytes -= 1

    return expected_bytes == 0
