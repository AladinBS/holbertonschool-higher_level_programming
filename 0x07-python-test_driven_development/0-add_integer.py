#!/usr/bin/python3
"""
Adding numbers
"""
def add_integer(a, b=98):
	""" 'add_integer(a, b)' allows to add an int and a float
        a
        b"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    	b = int(b)
	a = int(a)
    return (a + b)
