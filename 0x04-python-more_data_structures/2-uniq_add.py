#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqu = set(my_list)
    add = 0
    for i in uniqu:
        add += i
    return add
