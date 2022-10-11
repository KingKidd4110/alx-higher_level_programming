#!/usr/bin/python3
def raise_exception():
    x = "tekken"
    if not type(x) is int:
        raise TypeError("Only integers are allowed")
