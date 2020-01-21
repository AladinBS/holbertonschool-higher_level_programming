#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ Returns True or False in case the object
	is an inst of a_class
    Arguments:
    obj: This is an object
    a_class: This is a class type
    Ret:
    True if the object is
	an instance of a_class
    False, otherwise
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
