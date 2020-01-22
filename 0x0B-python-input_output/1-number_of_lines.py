#!/usr/bin/python3
""" Return the number of lines
"""
def number_of_lines(filename=""):
    """ Read from a file and nmbr of lines
        Exception: File opened
        filename: filename
    """
    x = 0
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            x += 1
    return x
