#!/usr/bin/python3
"""this module defines a square and initializes size as positive int
"""


class Square:
    """square implementation
    """
    def __init__(self, size=0):
        """Initializer
        Args:
            size: square size. Defaults to 0
        """
        self.size(size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """area of current square
        Returns:
            int: area of the square
        """
        return (self.__size ** 2)