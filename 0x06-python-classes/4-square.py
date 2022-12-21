#!/usr/bin/python3

"""Define a Class Square"""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new Square.
            Args:
                size (int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """Retrieve the size of Square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets/assigns a value to size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
