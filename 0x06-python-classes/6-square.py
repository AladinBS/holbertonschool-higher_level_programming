#!/usr/bin/python3
class Square:
    """ Define a square by size

    """
    def __init__(self, size=0, position=(0, 0)):
        """ Init the square object
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Return the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Position value
        
	"""
        return self.__position

    @position.setter
    def position(self, value):
        """ Value of a square object
        
	"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Returns the square are of the object
        
	"""
        return (self.__size ** 2)

    def my_print(self):
        """ Print a # square
        based on the size value

        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
