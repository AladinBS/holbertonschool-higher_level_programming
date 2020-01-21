#!/usr/bin/python3
class MyInt(int):
    """ Inherit class int"""
    def __eq__(self, other):
        """ Method for return != check """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ Method for return == check """
        return int.__eq__(self, other)
