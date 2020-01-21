#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """ Dfine a rect from BaseGeometry """
    def __init__(self, width, height):
        """ Init """
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width

    def area(self):
        """ Return area of the inst"""
        return self.__height * self.__width

    def __str__(self):
        """ Returns the printable str """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
