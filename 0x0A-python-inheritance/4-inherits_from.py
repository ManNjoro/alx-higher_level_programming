#!/usr/bin/python3
"""
Check if an object is an instance of a class that inherited
from the specified class.
"""


def inherits_from(obj, a_class):
    """
    This function returns True or False
    """
    return(issubclass(type(obj), a_class) and type(obj) is not a_class)
