"""Module containing Rectangle class."""
from models.base import Base

class Rectangle(Base):
    """Class to represent a rectangle deriving from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize new square with width, height, and offsets.

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): width offset for drawing rectangle
            y (int): height offset for drawing rectangle
            id: identifier for instance. If None, then object count

        Raise:
            TypeError: If `width`, `height`, `x`, or `y` are not ints.
            ValueError: If `width` or `height` are <= 0, or `x` or `y`
                are < 0.
        """
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
         
