#!/usr/bin/python3
"""Module to calculate calculate how many square units of water will be retained after it rains."""

def rain(array):
    total = 0
    first_wall = 0
    width = 0
    for i in array:
        if first_wall <= 0 and i > 0:
            first_wall = i
            width = 0
            continue
        if i > 0:
            print(total)
            total += (width * min(first_wall, i))
            first_wall = i
            width = 0
        else:
            width += 1
    return total
