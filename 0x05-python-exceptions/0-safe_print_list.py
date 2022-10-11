#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for x in my_list:
        x = x + 1
        try:
            print(x, end="")

        except IndexError:
            print("out of range")
