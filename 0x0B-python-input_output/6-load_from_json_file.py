#!/usr/bin/python3
import json
"""Defines a JSON file-reading function."""


def load_from_json_file(filename):
    """
    creates an Object from a JSON file
    """
    with open(filename) as f:
        return json.load(f)
