"""Module to represent Base object to be extended by Square and Rectangle."""


class Base:
    """Base class to be subclassed by Square and Rectangle"""
    __nb_object = 0
    """Class variable representing the total count of Base (and subclass)
    instances.
    """

    def __init__(self, id=None):
        """Initialize new Base instance

        Args:
            id: Identifier for instance. If None, use current object count.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object
             
