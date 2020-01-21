#!/usr/bin/python3
def add_attribute(obj, name, value):
    """ Function to add a new
    att to an obj
    Arguments:
    value: attribute value
    obj: object
    name: attribute name
    Raises:
    TypeError: if the att can't be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
