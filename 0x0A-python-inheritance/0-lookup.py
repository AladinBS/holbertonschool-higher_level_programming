#!/usr/bin/python3
def lookup(obj):
    """ Return a list of attributes
    Arguments:
    obj: an object instance of a class
    Ret:
    L of atts
    """
    return dir(obj)
