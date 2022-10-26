#!/usr/bin/python3
import json
"""
defines function
"""


def load_from_json_file(filename):
    with open(filename, "r", encoding="utf=8") as fl:
        """load obj from created json file"""
        return json.load(fl)
