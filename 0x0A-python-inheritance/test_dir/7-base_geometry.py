#!/usr/bin/python3
""" Empty Class of Shapes"""


class BaseGeometry:
    """ A class for all shape"""
    def area(self):

        """
        Area is not yet implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

         Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
         Raises:
            TypeError: If value is not an integer.
        """
        val = type(value)
        if val != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
