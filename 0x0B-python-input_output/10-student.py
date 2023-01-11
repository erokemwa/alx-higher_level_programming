#!/usr/bin/python3

""""instantiates a class and converts its items
to json representation"""


class Student:
    """defines a student including a method to
    represent the class in json"""

    def __init__(self, first_name, last_name, age):
        """instantiates the class object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """converts class attributes to jason
        representation"""
        if isinstance(attrs, list) and\
                all(isinstance(item, str) for item in attrs):
            result = {}
            for i in attrs:
                try:
                    result[i] = self.__dict__[i]
                except Exception:
                    pass
            return result
        elif attrs is None:
            return self.__dict__
