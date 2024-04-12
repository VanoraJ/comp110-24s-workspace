"""Practice writing a Twitter profile class."""


class Profile:
    username: str
    private: bool

    def __init__(self, username_input: str):  # No return type needed to declear
        """Create new profile"""
        self.username = username_input
        self.private = True

    def tweet(self, msg: str) -> None:
        """If Profile is NOT private, print msg."""
        if self.private == False:
            print(msg)


# Instatiation 
user1: Profile = Profile("110_rules")  # __init__
user1.private = False
user1.tweet("OOP is cool!")