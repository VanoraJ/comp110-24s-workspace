"""File to define Bear class."""

__author__ = "730653557"


class Bear:
    """Definig the Class Bear."""
    
    age: int
    hunger_score: int
    
    def __init__(self):
        """Constructing the Bear class object."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Bear passing one day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Increasing hunger score based on number of fish ate."""
        self.hunger_score += num_fish
        return None