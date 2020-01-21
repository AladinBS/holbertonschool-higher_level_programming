#!/usr/bin/python3
class BaseGeometry:
    """ This class defines atts of Geo Shapes """
    def area(self):
        """ This method defines an area of geo shapes """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This method recieves value prop
        Args:
        name: of object
        value: value of prop
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
