#!/usr/bin/python3
import json
"""
Function that writes an obj to a text file using
JSON rep
"""


def save_to_json_file(my_obj, filename):
    """
    function that writes an obj  to a text file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
