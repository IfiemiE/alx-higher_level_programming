#!/usr/bin/python3
# Author: Erigi Ifiemi

"""Define a Class Square."""


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
        """Sets and Gets the current size of Square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        if self__size != 0:
            for i in range(0, self.__size):
                for j in range(self.__size):
                    print("#", end="")

                print("")
        else:
            print("")
