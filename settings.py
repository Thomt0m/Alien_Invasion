# General settings for alien_invasion game

class Settings:
    """A class containing all general settings for Alien Invasion"""


    def __init__(self) -> None:
        """Initialise the game's settings"""



        # ---- Screen ----
        self.screen_width = 1920
        self.screen_height = 1080
        self.background_colour = (230, 230, 230)

        
        # ---- Ship (player) entity ----
        # Size to scale an image of a ship to, relative to (vertical) screen size
        self.ship_image_scale = 0.1
        # Multiplier of movement distance of ship, speed is determined relative to the width of the screen, comfortable values are around '0.001'
        self.ship_speed_multiplier = 0.002


        # ---- Bullet ----
        # Multiplier of movement distance of bullet, speed is determined relative to the height of the screen, comfortable values are around '0.002'
        self.bullet_speed = 8
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)

