#!/usr/bin/python3
""" Return an object by a JSON rep
"""
import json
def from_json_string(my_str):
    """ Return an object by a JSON rep
        Except: string UNdecoded
        my_str: JSON rep
    """
    return json.loads(my_str)
