#!/usr/bin/python3
"""
A student class with public attributes and retrives
json dictionary rep
"""


class Student:
    """
    student class with public instances
    """
    def __init__(self, first_name, last_name, age):
        """
        instantiation of attribute
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        function returns dict representation of instance
        """
        if attrs is None:
            return (self.__dict__)
        return ({key: value for key, value in self.__dict__.items()
                 if key in attrs})
