#!/usr/bin/python3
"""
Rectangle
"""
class Rectangle:
    """
	width: rect wid
	height: rect hei
    """
    def __init__(self, width=0, height=0):
        """
		width: rect wid
		height: rect hei
		"""
        self.height = height
        self.width = width

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Must be an integer")
        if value < 0:
            raise ValueError("Must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Must be an integer")
        if value < 0:
            raise ValueError("Must be >= 0")
        self.__height = value

    def area(self):
        return (self.height * self.width)

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return (0)
        return (2 * (self.height + self.width))

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ("")
        rec = ""
        for i in range(self.height):
            for j in range(self.width):
                rec = rec + "#"
            rec = rec + "\n"
        return(rec[:-1])
