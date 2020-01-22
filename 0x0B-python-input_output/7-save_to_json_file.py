#!/usr/bin/python3
""" writes object to a txt file using JSON
"""
import json
def save_to_json_file(my_obj, filename):
    """ an object to a text file by JSON rep
        filename: text name
        Excep: object unencoded
        my_obj: object
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
