#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """ Return True or False if the object is an instance of a_class
    Arguments:
	a_class: this is a class type
    obj: this is an object
    Returns:
        True in case the object is an instance of a_class
        False, otherwise
    """
    return isinstance(obj, a_class)
