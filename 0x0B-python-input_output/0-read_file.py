#!/usr/bin/python3
""" Read from a file """
def read_file(filename=""):
    """ Read from a file
        Exception: file opened
        filename: filename
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
