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

        # On a continous loop
        while True:

            self._check_events()
            self._update_elements()
            self._update_screen()


            











    def _check_events(self) -> None:
        """Checks for events from pygame, eg keyboard or mouse input. Called constantly"""

        # Go over all pygame events that happened last frame
        for event in pygame.event.get():
            match event.type:

                case pygame.QUIT:
                    sys.exit()

                case pygame.KEYDOWN:
                    match event.key:

                        case pygame.K_RIGHT:
                            # Move the player's ship to the right
                            self.ship.moving_right = True
                        case pygame.K_LEFT:
                            # Move the player's ship to the left
                            self.ship.moving_left = True

                case pygame.KEYUP:
                    match event.key:

                        case pygame.K_RIGHT:
                            # Stop the player's ship moving to the right
                            self.ship.moving_right = False
                        case pygame.K_LEFT:
                            # Stop the player's ship moving to the left
                            self.ship.moving_left = False
                            





    def _update_elements(self) -> None:
        """Update elements of the game. Called constantly"""
        
        self.ship.update_pos()






    def _update_screen(self) -> None:
        """Update the elements on screen, and redraw the updated screen. Called constantly"""

        # Redraw the screen, and all its attributes/elements
        # !ORDER MATTERS! Everything gets drawn in order, so things further down will be drawn on top of their predecesors
        self.screen.fill(self.settings.background_colour)
        self.ship.blitme()

        # Make the newly drawn screen visible, ie update
        pygame.display.flip()








if __name__ == '__main__':
    # Create an instance of the game, and run it
    game = AlienInvasion()
    game.run_game()