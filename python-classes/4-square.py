#!/usr/bin/python3
"""Defines a Square class with size getter and setter."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        self.size = size   # uses the setter below, so validation runs here too

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square, with validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size * self.__size
