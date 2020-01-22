#!/usr/bin/python3
""" JSON rep of an object
"""
import json
def to_json_string(my_obj):
    """ Return the JSON rep
        Except: object can't be encoded
        my_obj: object
    """
    return json.dumps(my_obj)
