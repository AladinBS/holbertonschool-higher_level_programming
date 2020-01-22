#!/usr/bin/python3
""" 
	Appends to text file
"""
def append_write(filename="", text=""):
    """ Appends to a file
        text: text
        Except: file can be opened
        filename: filename
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
