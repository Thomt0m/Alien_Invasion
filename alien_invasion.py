# Alien Invasion, written by Thomas A.
# Based on the project 'Alien Invasion' from the book 'Python Crash Course, 2nd edition'





# ---- External ----
# System
from os import truncate
import sys
from time import sleep
# Pygame, set of modules for video games 
import pygame



# ---- Custom, home-made ----
# General game-settings class
from settings import Settings
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from ship import Ship
from bullet import Bullet
from alien import Alien








class AlienInvasion:
    """Base class, manages game assets and behaviour"""
    


    def __init__(self) -> None:
        """Initialise the game, and create its resources"""

        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Alien Invasion")

        self.settings = Settings(self.screen.get_rect())
        self.settings.screen.width = self.screen.get_rect().width
        self.settings.screen.height = self.screen.get_rect().height

        self.stats = GameStats(self)
        self.play_button = Button(self, message="Play")
        self.scoreboard = Scoreboard(self)

        # Create the player ship
        self.ship = Ship(self, self.settings.ship.image_scale)
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
            if self.stats.game_active:
                self._update_elements()
            self._update_screen()
            






            




    def new_game(self):
        """Start a new game of alien invasion. Resets player pos, bullets and aliens"""
        self.aliens.empty()
        self.bullets.empty()
        self._create_alien_fleet()
        self.ship.center_ship()
        self.scoreboard.player_lives_to_image()
        self.scoreboard.level_to_image()











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

                # Mouse down events
                case pygame.MOUSEBUTTONDOWN:
                    self._handle_mousebuttondown_event(event)



    def _handle_keydown_event(self, event: pygame.event.Event) -> None:
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

    def _handle_keyup_event(self, event: pygame.event.Event) -> None:
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

    def _handle_mousebuttondown_event(self, event: pygame.event.Event):
        """Handle the specified MouseButtonDown event. Acts based on mouse position"""
        mouse_pos = pygame.mouse.get_pos()
        if self.stats.game_active is False:
            self._check_play_button_clicked(mouse_pos)
        



                            





    def _update_elements(self) -> None:
        """Update elements of the game. Called constantly"""
        
        self._update_ship()
        self._update_bullets()
        self._update_aliens()



    def _update_ship(self) -> None:
        """Update the player ship"""
        self.ship.update_pos()

    def _update_bullets(self) -> None:
        """Update the bullets fired by player"""
        self.bullets.update()
        # Loop over all bullets, delete those that are out-of-bounds (python expects the list of bullets to remain unchanged for the duration of the for-loop, so we make a copy of bullets that wont change for the loop to iterate through, and now we can safely make changes to bullets)
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_aliens_hit_by_bullets()
       

    def _check_aliens_hit_by_bullets(self):
        """Check if any aliens were hit by a bullet, and if so remove both from play"""
        # Check for any bullets that have hit aliens, if so, destroy both
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien.points * len(aliens)
            self.scoreboard.score_to_image()
        # If no aliens are left, delete any remaining bullets and create a new alien fleet
        if not self.aliens:
            self.settings.increase_difficulty()
            self.stats.level += 1
            self.new_game()
            

    def _update_aliens(self):
        """Update the fleet of aliens"""
        self._check_alien_fleet_edges()
        self.aliens.update()

        # Check if any aliens have collided with the player ship, meaning this game is lost
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._player_lost()

        # Check if any aliens have reached the bottom of the screen, meaning this game is lost
        self._check_alien_fleet_bottom()






    def _update_screen(self) -> None:
        """Update the elements on screen, and redraw the updated screen. Called constantly"""

        # ---- Redraw the scene on screen, and all its attributes/elements  ----
        # ---- ORDER MATTERS! Everything gets drawn in order, top down      ----
        # ---- Things further down will be drawn over their predecesors     ----

        # Set the background, fill with simple colour
        self.screen.fill(self.settings.screen.background_colour)
        # Draw the player ship
        self.ship.blit_me()
        # Draw the bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Draw the alien fleeet
        self.aliens.draw(self.screen)
        self.scoreboard.show_score()

        # If the game if 'inactive', draw the 'Play' button
        if not self.stats.game_active:
            self.play_button.draw_button()

        # ---- End of drawing ----


        # Make the newly drawn screen visible, ie update
        pygame.display.flip()










    def _fire_bullet(self) -> None:
        """Create a new bullet, add it to 'bullets' group"""
        if (self.settings.bullet.limit_number and len(self.bullets) >= self.settings.bullet.max_number_allowed) == False:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _create_alien_fleet(self, rows: int = 2, columns: int = 9999):
        """Create a fleet of alien ships"""
        # Create an alien ship and find the number of ships that will fit in a row, and a column, depending on screen width
        alien = Alien(self, self.settings.screen.height * self.settings.alien.image_scale)
        edge_margin_hor = self.settings.alien.edge_margin_hor * self.settings.screen.width
        # Floor-division, aka integer division, might return a float although the value should always be a whole number, ie an integer. But 'for alien_num in range(max_aliens_in_row)' starts protesting when recieving a float, so we cast to int
        max_aliens_in_row = int((self.settings.screen.width - 2 * edge_margin_hor) // (self.settings.alien.fleet_spacing * alien.rect.width))
        edge_margin_vert = self.settings.alien.edge_margin_vert * self.settings.screen.width
        # Maximum vertical size of the fleet is limited to the height of the screen, minus 2 * the height of the players ship
        max_aliens_in_column = int((self.settings.screen.height - edge_margin_vert - self.ship.rect.height * 2) // (2 * alien.rect.height))
                
        # Clamp rows to the maximum number of columns that will fit on screen (ie the max vertical length)
        rows = max(1, min(rows, max_aliens_in_column))
        # Clamp columns to the maximum number of rows that will fit on screen (ie the max horizontal length)
        columns = max(1, min(columns, max_aliens_in_row))

        # Store the current edge_margin_hor, decreased by a buffer
        self.settings.alien.edge_distance_hor = edge_margin_hor / 3

        # Create the fleet of aliens, setting x and y for each alien
        for alien_m in range(rows):
            for alien_n in range(columns):
                # Create an alien ship, set its screen location, and place it in the aliens group
                alien = Alien(self, self.settings.screen.height * self.settings.alien.image_scale)
                alien.set_initial_pos(
                    edge_margin_hor + self.settings.alien.fleet_spacing * alien.rect.width * alien_n, 
                    edge_margin_vert + self.settings.alien.fleet_spacing * alien.rect.height * alien_m)
                self.aliens.add(alien)

    
    def _check_alien_fleet_edges(self):
        """Check if the edge of the alien fleet is at/near the horizontal edge of the screen"""
        for alien in self.aliens.sprites():
            if alien.is_at_hor_screen_edge():
                self._change_alien_fleet_direction()
                break

    def _check_alien_fleet_bottom(self):
        """Check if a alien of the alien fleet has reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # End the game
                self._player_lost()
                break


    def _change_alien_fleet_direction(self):
        """Make the fleet move down, and change the direction of horizontal movement of the alien fleeet"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien.speed_y
        self.settings.alien.fleet_movement_direction *= -1

    
    def _check_play_button_clicked(self, mouse_pos):
        """Check if the player clicked the 'Play' button, if so set game_active to true"""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.reset_stats()            
            self.settings.reset_speed()
            self.stats.game_active = True
            self.scoreboard.score_to_image()
            pygame.mouse.set_visible(False)
            self.new_game()


    def _player_lost(self):
        """
        This game has been lost, eg because the player ship is hit by an alien, or an alien has reached the bottom of the screen.
        Decrement the players lives by one, and remove any residual aliens and bullets, then start a new round
        """
        # If the player has any lives left
        if self.stats.lives > 1:
            self.stats.lives -= 1
            self.new_game()
            # Give the player time to recognise this round was lost
            sleep(1.0)
        # Else the game is over
        else:
            self.stats.game_active = False
            if self.stats.score > self.stats.highscore:
                self.stats.highscore = self.stats.score
            pygame.mouse.set_visible(True)












if __name__ == '__main__':
    # Create an instance of the game, and run it
    game = AlienInvasion()
    game.run_game()