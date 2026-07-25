#!/usr/bin/python3
"""Defines a BaseGeometry class with an unimplemented area method."""


class BaseGeometry:
    """Represent a base geometry shape."""

    def area(self):
        """Raise an Exception, since area computation is not defined here."""
        raise Exception("area() is not implemented")
