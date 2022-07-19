#!/usr/bin/python3
"""this module defines a square and initializes size as positive int
"""


class Square:
    """square implementation
    """
    def __init__(self, size=0):
        if !(isinstance(size, int)):
            raise TypeError('size must be an integer')
        elif size <= 0:
            raise ValueError('size must be >= 0')
        self.__size = size
