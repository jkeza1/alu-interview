#!/usr/bin/python3
"""
minOperations module

This module provides a method to calculate the fewest
number of operations required to obtain a desired count
of H characters in a file, given the operations Copy All and Paste.

"""
import math


def minOperations(n):
    """
    Calculates the fewest number of operations required to
    obtain exactly n H characters in the file.

    Parameters:
        n (int): The desired count of H characters.

    Returns:
        int: The minimum number of operations required.
        If n is impossible to achieve or invalid(negative), returns 0.

    """
    if n <= 0:
        return 0

    operations = 0

    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            operations += i
            n = n // i

    if n > 1:
        operations += n

    return operations
