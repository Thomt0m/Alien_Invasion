# General settings for alien_invasion game




import pygame


class Settings:
    """A class containing all general settings for Alien Invasion"""


    # ---- Screen Settings ----
    class ScreenSettings:
        """Settings related to the screen"""

        def __init__(self) -> None:
            """Initialise screen settings"""
            self.width = 1920
            self.height = 1080
            self.background_colour = (40, 40, 40)




    # ---- Player Ship Settings ----
    class PlayerShipSettings:
        """Settings related to the player ship"""

        def __init__(self, screen_width: int) -> None:
            """Initialise player ship settings"""
            # Size to scale an image of a ship to, relative to (vertical) screen size
            self.image_scale = 0.1
            # Multiplier of movement distance of ship, speed is determined relative to the width of the screen, speed is expressed as pixels per frame, comfortable values are around '0.001'
            self.speed_multiplier = 0.002
            self.speed_x_base: float = screen_width * self.speed_multiplier
            self.speed_x: float = self.speed_x_base
            self.max_lives = 3
        



    # ---- Bullet Settings
    class BulletSettings:
        """Settings related to bullets"""

        def __init__(self) -> None:
            """Initialise bullet settings"""
            self.speed_base: float = 8
            self.speed: float = self.speed_base
            self.width = 3
            self.height = 15
            self.colour = (250, 250, 250)
            self.limit_number = True
            self.max_number_allowed = 3




    class AlienSettings:
        """Settings related to the alien ship"""

        def __init__(self, screen_rect: pygame.rect) -> None:
            """Initialise alien ship settings"""
            # Size to scale an image of a ship to, relative to (vertical) screen size
            self.image_scale = 0.05
            # The space between the outer alien entity and the edge of the screen, expressed as a fraction of the screen width (for horizontal and vertical)
            self.edge_margin_hor = 0.06
            self.edge_margin_vert = 0.01
            # Spacing between alien ships in the fleet, expressed alien-ship-widths (actual space is minus one, since each ship takes up its own width)
            self.fleet_spacing = 1.6
            # Multiplier of movement distance of alien ship, speed is determined relative to the width of the screen, speed is expressed as pixels per frame, comfortable values are around '0.0002'
            self.speed_hor_multiplier = 0.0002
            self.speed_x_base: float = screen_rect.width * self.speed_hor_multiplier
            self.speed_x: float = self.speed_x_base
            # Vertical speed is done as a single step, instead of a continuous movement
            self.speed_ver_multiplier = 0.01
            self.speed_y_base: float = screen_rect.height * self.speed_ver_multiplier
            self.speed_y: float = self.speed_y_base
            print(f"Settings: alien.speed_y = {self.speed_y}")
            # Movement direction of the alien fleet, 1 == moving to the right, -1 == moving to the left
            self.fleet_movement_direction = 1
            # Actual distance in pixels from the edge of the screen
            self.edge_distance_hor = 0.0
            
            










    def __init__(self, screen_rect: pygame.rect) -> None:
        """Initialise the game's settings"""

        self.screen = Settings.ScreenSettings()
        self.ship = Settings.PlayerShipSettings(screen_rect.width)
        self.bullet = Settings.BulletSettings()
        self.alien = Settings.AlienSettings(screen_rect)

        # ---- General settings ----
        # Increase factor of game speed after each succesfull round
        self.speed_scale = 1.1





    def increase_speed(self):
        """Increase the speed of the player ship, bullets and the alien fleet"""
        self.ship.speed_x *= self.speed_scale
        self.bullet.speed *= self.speed_scale
        self.alien.speed_x *= self.speed_scale
        self.alien.speed_y *= ((self.speed_scale - 1) / 4) + 1
        print("Settings: speed increased")

    def reset_speed(self):
        """Reset the speed of the player ship, bullets and the alien fleet back to their initial values"""
        self.ship.speed_x = self.ship.speed_x_base
        self.bullet.speed = self.bullet.speed_base
        self.alien.speed_x = self.alien.speed_x_base
        self.alien.speed_y = self.alien.speed_y_base
        print("Settings: speed reset")


