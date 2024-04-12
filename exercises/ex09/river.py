"""File to define River class."""

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear

__author__ = "730653557"


class River:
    """Defining Class River."""    
    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checking the survived fish and bear based on age."""
        surviving_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        self.fish = surviving_fish

        surviving_bears: list[Bear] = []
        for bears in self.bears:
            if bears.age <= 5:
                surviving_bears.append(bears)
        self.bears = surviving_bears

        return None

    def bears_eating(self):
        """Bears eating 3 fish if there is at least 5 fish."""
        for bears in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bears.eat(3)

        return None
    
    def check_hunger(self):
        """Creating a surviving bear list to check for bear's hunger score."""
        surviving_bears: list[Bear] = []
        for bears in self.bears:
            if bears.hunger_score >= 0:
                surviving_bears.append(bears)
        self.bears = surviving_bears

        return None
        
    def repopulate_fish(self):
        """Repopulating fish if there are at least 2 fish."""
        num_fish: int = len(self.fish)
        num_new_borns: int = (num_fish // 2) * 4

        for index in range(0, num_new_borns):
            new_fish: Fish = Fish()
            self.fish.append(new_fish)
        
        return None
    
    def repopulate_bears(self):
        """Repopulating bears if there are at least 2 bears."""
        num_bears: int = len(self.bears)
        num_new_borns: int = num_bears // 2

        for index in range(0, num_new_borns):
            new_bear: Bear = Bear()
            self.bears.append(new_bear)

        return None
    
    def view_river(self):
        """Printing out basic info of population and date."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}") 
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Running the one_river_day function 7 times."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day() 
        return None
    
    def remove_fish(self, amount: int):
        """Removing amount number of fish from the front of the fish list."""
        for idx in range(0, amount):
            self.fish.pop(0)
        return None
