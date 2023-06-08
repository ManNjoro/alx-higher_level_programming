#!usr/bin/python3
"""
Prints the name in the format 'My name is <first name> <last name>'.
"""


def say_my_name(first_name, last_name=""):
    """

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError(
            "first_name must be a string or last_name must be a string")

    full_name = " ".join([part for part in [first_name, last_name] if part])
    print("My name is {} {}". format(first_name, last_name))
