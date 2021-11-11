# Alien Invasion, written by Thomas A.
# Based on the project 'Alien Invasion' from the book 'Python Crash Course, 2nd edition'


# ---- External ----
# System
import sys
# Pygame, set of modules for video games 
import pygame

# ---- Custom ----
# General game-settings class
from settings import Settings
from ship import Ship



class AlienInvasion:
    """Base class, manages game assets and behaviour"""
    

    def __init__(self) -> None:
        """Initialise the game, and create its resources"""

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)


        # Set background colour (TODO replace with image or something)
        self.bg_colour = (230, 230, 230)




    def run_game(self) -> None:
        """Run the main game loop"""

        while True:

            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


            # Redraw the screen, and all its attributes/elements
            # !ORDER MATTERS! Everything gets drawn in order, so things further down will be drawn on top of their predecesors
            self.screen.fill(self.settings.background_colour)
            self.ship.blitme()

            # Make the most recently drawn screen visible
            pygame.display.flip()








if __name__ == '__main__':
    # Create an instance of the game, and run it
    game = AlienInvasion()
    game.run_game()