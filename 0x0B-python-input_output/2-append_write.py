#!/usr/bin/python3
"""
Defines function append_write
"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding="utf=8") as fl:
        return fl.write(text)
