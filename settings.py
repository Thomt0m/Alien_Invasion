# General settings for alien_invasion game

class Settings:
    """A class containing all general settings for Alien Invasion"""


    def __init__(self) -> None:
        """Initialise the game's settings"""



        # ---- Screen settings ----
        self.screen_width = 1920
        self.screen_height = 1080
        self.background_colour = (230, 230, 230)

        
        # ---- Ship (player) entity values ----
        # Size to scale an image of a ship to, relative to screen size
        self.ship_image_scale = 10
        # Multiplier of movement distance of ship, speed is determined relative to the width of the screen, comfortable values are around '0.001'
        self.ship_speed_multiplier = 0.001

