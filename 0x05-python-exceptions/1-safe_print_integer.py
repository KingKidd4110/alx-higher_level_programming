#!/usr/bin/python3
def safe_print_integer(value):
    a = value
    try:
        print("{:d}".format(a))
    except TypeError:
        return False
    else:
        return True
