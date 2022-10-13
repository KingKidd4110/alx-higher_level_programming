#!/usr/bin/python3
"""Class Square"""


class Square:
    """A square
    Attributes:
        _size (int): side measure of square
    """

    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): side size
        Returns:
            None
        """
        self.size = size

    def area(self):
        """calculates the area of the square
        Returns:
            Area
        """
        return (self._size) ** 2

    @property
    def size(self):
        """getter of _size
        Returns:
            Square size
        """
        return self._size

    @size.setter
    def size(self, value):
        """_size setter
        Args:
            value (int): the size of side
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self._size = value
