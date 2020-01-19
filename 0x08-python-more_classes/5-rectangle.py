#!/usr/bin/python3
class Rectangle:
    """ Rectangle """
    def __init__(self, width=0, height=0):
        """
        width: rect wid
        height: rect hei
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """
        value: wid
		TypeError: must be an integer
		ValueError: must not be negative
        """
        if not isinstance(value, int):
            raise TypeError("It must be an integer")
        if value < 0:
            raise ValueError("It must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("It must be an integer")
        if value < 0:
            raise ValueError("It must be > 0")
        self.__height = value

    def area(self):
        """ Calc the area
            and returns the rect area
        """
        return self.height * self.width

    def perimeter(self):
        """ Calc the Rect perimeter
            and returns the rect perim
        """
        if self.width == 0 or self.height == 0:
            return 0
        return ((2 * self.width) + 2 * self.height) 

    def __str__(self):
		rectangle = ""
        if self.height == 0 or self.width == 0:
            return rectangle

        for x in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ Returns the str repr of inst
        and returns
        """

        return "Rect({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
