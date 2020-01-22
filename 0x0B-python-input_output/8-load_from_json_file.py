#!/usr/bin/python3
""" Object from a JSON
"""
import json
def load_from_json_file(filename):
    """ Create an Object from JSON
        Except: Object unencoded
        filename: file name
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
