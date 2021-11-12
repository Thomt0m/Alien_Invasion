# Alien Invasion, written by Thomas A.
# Based on the project 'Alien Invasion' from the book 'Python Crash Course, 2nd edition'


# ---- External ----
# System
import sys
# Pygame, set of modules for video games 
import pygame

# ---- Custom, home-made ----
# General game-settings class
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien



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
        self.ship = Ship(self, self.settings.screen_height * self.settings.ship_image_scale)
        # Create a group for the bullets fired by the player
        self.bullets = pygame.sprite.Group()
        # Create a group for the aliens
        self.aliens = pygame.sprite.Group()
        self._create_alien_fleet()








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

            # Fire bullets
            case pygame.K_SPACE:
                self._fire_bullet()

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
        
        self._update_ship()
        self._update_bullets()



    def _update_ship(self) -> None:
        """Update the player ship"""
        self.ship.update_pos()

    def _update_bullets(self) -> None:
        """Update the bullets fired by player"""
        self.bullets.update()
        # loop over all bullets, delete those that are out-of-bounds (python expects the list of bullets to remain unchanged for the duration of the for-loop, so we make a copy of bullets that wont change for the loop to iterate through, and now we can safely make changes to bullets)
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)






    def _update_screen(self) -> None:
        """Update the elements on screen, and redraw the updated screen. Called constantly"""

        # Redraw the screen, and all its attributes/elements
        # !ORDER MATTERS! Everything gets drawn in order, so things further down will be drawn on top of their predecesors
        self.screen.fill(self.settings.background_colour)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Make the newly drawn screen visible, ie update
        pygame.display.flip()










    def _fire_bullet(self) -> None:
        """Create a new bullet, add it to 'bullets' group"""
        if (self.settings.bullet_limit_number and len(self.bullets) >= self.settings.bullet_max_number_allowed) == False:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    # TODO remove, old, replaced by _create_fleet
    def _add_alien_to_fleet(self) -> None:
        """Add an alien to the alien fleet"""
        alien = Alien(self, self.settings.screen_height * self.settings.ship_image_scale)
        self.aliens.add(alien)

    def _create_alien_fleet(self, rows = 1):
        """Create a fleet of alien ships"""
        # Create an alien ship and find the number of ships that will fit in a row, and a column, depending on screen width
        alien = Alien(self, self.settings.screen_height * self.settings.ship_image_scale)
        edge_margin_hor = self.settings.alien_edge_margin_hor * alien.rect.width
        # Floor-division, aka integer division, might return a float although the value should always be a whole number ('for alien_num in range(max_aliens_in_row)' starts protesting without casting to int)
        max_aliens_in_row = int((self.settings.screen_width - 2 * edge_margin_hor) // (self.settings.alien_fleet_spacing * alien.rect.width))
        edge_margin_vert = self.settings.alien_edge_margin_vert * alien.rect.height
        max_aliens_in_column = int((self.settings.screen_height / 2 - edge_margin_vert) // (2 * alien.rect.height))

        # Clamp rows to the maximum number of columns that will fit on screen
        rows = max(1, min(rows, max_aliens_in_column))

        # Create the rows of aliens
        i = 0
        while i < rows:
            for alien_num in range(max_aliens_in_row):
                # Create an alien ship, set its location on screen, and place it in the aliens group
                alien = Alien(self, self.settings.screen_height * self.settings.ship_image_scale)
                alien.rect.x = edge_margin_hor + self.settings.alien_fleet_spacing * alien.rect.width * alien_num
                alien.rect.y = edge_margin_vert + self.settings.alien_fleet_spacing * alien.rect.height * i
                self.aliens.add(alien)
            i += 1











if __name__ == '__main__':
    # Create an instance of the game, and run it
    game = AlienInvasion()
    game.run_game()