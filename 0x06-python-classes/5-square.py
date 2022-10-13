#!/usr/bin/python3
"""Class Square"""


class Square:
    """Represents a square
    Attributes:
        _size (int): size of a side of the square
    """

    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """calculates the square's area
        Returns:
            The area of the square
        """
        return (self._size) ** 2

    @property
    def size(self):
        """getter of _size
        Returns:
            The size of the square
        """
        return self._size

    @size.setter
    def size(self, value):
        """setter of _size
        Args:
            value (int): size of a side of the square
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

    def my_print(self):
        """prints the square
        Returns:
            None
        """
        if self._size == 0:
            print()
            return
        for i in range(self._size):
            print("".join(["#" for j in range(self._size)]))
