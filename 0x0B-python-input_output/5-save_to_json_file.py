#!/usr/bin/python3
import json
"""
defines function 
"""


def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf=8") as fl:
        """write obj file"""
        json.dump(my_obj, fl)
