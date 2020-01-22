#!/usr/bin/python3
""" Function that reads n lines
"""
def read_lines(filename="", nb_lines=0):
    """ Read from a file and nmbr of lines
        Except: file opened
        filename: filename
        nb_lines: line nmbr
    """
    with open(filename, 'r', encoding="utf-8") as f:
        if nb_lines <= 0:
            read_data = f.read()
            print(read_data, end='')
        else:
            n_lines = 0
            for x in f:
                print(x, end='')
                n_lines += 1
                if n_lines == nb_lines:
                    break
