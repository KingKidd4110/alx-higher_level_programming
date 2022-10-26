#!/usr/bin/python3
import json
"""
defines func from_json_string
"""


def from_json_string(my_str):
    """
    return
    object rep by json str
    """
    return json.loads(my_str)
