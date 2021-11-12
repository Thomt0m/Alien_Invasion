# General settings for alien_invasion game

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

        def __init__(self) -> None:
            """Initialise player ship settings"""
            # Size to scale an image of a ship to, relative to (vertical) screen size
            self.image_scale = 0.1
            # Multiplier of movement distance of ship, speed is determined relative to the width of the screen, speed is expressed as pixels per frame, comfortable values are around '0.001'
            self.speed_multiplier = 0.002
        



    # ---- Bullet Settings
    class BulletSettings:
        """Settings related to bullets"""

        def __init__(self) -> None:
            """Initialise bullet settings"""
            self.speed = 8
            self.width = 3
            self.height = 15
            self.colour = (250, 250, 250)
            self.limit_number = True
            self.max_number_allowed = 3




    class AlienSettings:
        """Settings related to the alien ship"""

        def __init__(self) -> None:
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
            self.speed_ver_multiplier = 0.002
            # Movement direction of the alien fleet, 1 == moving to the right, -1 == moving to the left
            self.fleet_movement_direction = 1
            
            





    def __init__(self) -> None:
        """Initialise the game's settings"""

        self.screen = Settings.ScreenSettings()
        self.ship = Settings.PlayerShipSettings()
        self.bullet = Settings.BulletSettings()
        self.alien = Settings.AlienSettings()


        # ---- Alien ----
        # Size to scale an image of a ship to, relative to (vertical) screen size
        #self.alien_image_scale = 0.05
        # The space between the outer alien entity and the edge of the screen, expressed as a fraction of the screen width (for horizontal and vertical)
        #self.alien_edge_margin_hor = 0.06
        #self.alien_edge_margin_vert = 0.01
        # Spacing between alien ships in the fleet, expressed alien-ship-widths (actual space is minus one, since each ship takes up its own width)
        #self.alien_fleet_spacing = 1.6
        # Multiplier of movement distance of alien ship, speed is determined relative to the width of the screen, speed is expressed as pixels per frame, comfortable values are around '0.0002'
        #self.alien_speed_hor_multiplier = 0.0002
        #self.alien_speed_ver_multiplier = 0.002
        # Movement direction of the alien fleet, 1 == moving to the right, -1 == moving to the left
        #self.alien_fleet_movement_direction = 1


