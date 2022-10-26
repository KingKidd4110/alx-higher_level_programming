#!/usr/bin/python3
""" Defines func to add attribute"""


def add_attr(obj, attr, value):
    """

    :param obj: initial obj to be added an attr
    :param attr: (str)
    :param value: value
    :return:  nothing

    :raises TypeError
    """
    if not hasattr(obj, "__dict__"):
        """raise"""
        raise TypeError("can't add new attribute")
    """return"""
    setattr(obj, attr, value)
