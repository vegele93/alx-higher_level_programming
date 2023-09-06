#!/usr/bin/python3
"""
    This module prints the first name and last name in the argument
"""


def say_my_name(first_name, last_name=""):
    """
        A function that printts first name and last name

        Args:
            first_name (string): first name
            last_name (string): last name

        Returns:
            None
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
