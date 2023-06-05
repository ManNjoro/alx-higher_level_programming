#!/usr/bin/python3
"""Define a class square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """
        Args:
            size (int): The size of the new square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size