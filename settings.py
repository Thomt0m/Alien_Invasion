# General settings for alien_invasion game

class Settings:
    """A class containing all general settings for Alien Invasion"""


    def __init__(self) -> None:
        """Initialise the game's settings"""


        # CONSTANTS
        # Size to scale an image of a ship to
        self.IMAGE_SCALE_SHIP = 150


        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_colour = (230, 230, 230)

