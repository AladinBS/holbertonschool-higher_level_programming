#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """ This class defines a rect from BaseGeometry Class """
    def __init__(self, width, height):
        """ Initit """
	self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
	self.__width = width
