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

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # Create the player ship
        self.ship = Ship(self, self.settings.screen_height / self.settings.ship_image_scale)


        # Set background colour (TODO replace, with generated or image or something)
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

                # Close window event, quit
                case pygame.QUIT:
                    sys.exit()


                # Key down events
                case pygame.KEYDOWN:
                    self._handle_keydown_event(event)

                # Key up events
                case pygame.KEYUP:
                    self._handle_keyup_event(event)


    def _handle_keydown_event(self, event) -> None:
        """Handle the specified KeyDown event. Acts based on the key that triggered the event"""
        match event.key:

            # On escape, quit game (TODO determine if a pause menu should be on escape)
            case pygame.K_ESCAPE:
                sys.exit()
            # On backspace, quit game
            case pygame.K_BACKSPACE:
                sys.exit()

            # Move the player's ship to the right
            case pygame.K_RIGHT:
                self.ship.moving_right = True
            case pygame.K_d:
                self.ship.moving_right = True
                
            # Move the player's ship to the left
            case pygame.K_LEFT:
                self.ship.moving_left = True
            case pygame.K_a:
                self.ship.moving_left = True

    def _handle_keyup_event(self, event) -> None:
        """Handle the specified KeyUp event. Acts based on the key that triggered the event"""
        match event.key:

            # Stop the player's ship moving to the right
            case pygame.K_RIGHT:
                self.ship.moving_right = False
            case pygame.K_d:
                self.ship.moving_right = False

            # Stop the player's ship moving to the left
            case pygame.K_LEFT:
                self.ship.moving_left = False
            case pygame.K_a:
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