#!/usr/bin/python3
""" Return dict descrip for a JSON object
"""
def class_to_json(obj):
    """ Retuns the descrip of obj """
    x = {}
    if hasattr(obj, "__dict__"):
        x = obj.__dict__.copy()
    return x
