#!/usr/bin/python3
def is_same_class(obj, a_class):

    """ Return True or False incase the obj is a a_class
    Argumentss:
    obj: an object
    a_class: the class type
    Rets:
    True when type is a_class
    False, otherwise
    """
    return type(obj) is a_class
