#!/usr/bin/python3
"""
Function to find and return the maximum integer in a list.
"""


def max_integer(lst=[]):
    """
    Args:
        lst (list): List of integers.

    Returns:
        int: Maximum integer in the list. If the list is empty, returns None.
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) == 0:
        return None
    result = lst[0]
    for num in lst:
        if num > result:
            result = num
    return result
