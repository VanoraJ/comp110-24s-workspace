"""File to define Fish class."""

__author__ = "730653557"


class Fish:
    """Defining the class Fish."""
    
    age: int

    def __init__(self):
        """Constructing the Fish class object."""
        self.age = 0
        return None
    
    def one_day(self):
        """Fish passing one day."""
        self.age += 1
        return None