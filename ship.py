import pygame


class Ship:
    """Player's ship, manages the ship"""


    def __init__(self, game) -> None:
        """Initialise a ship, and set its starting position"""

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load the ship image and get its rectangle
        self.image = pygame.image.load("Assets/Spaceship01.png")
        self.image = pygame.transform.scale(self.image, (game.settings.IMAGE_SCALE_SHIP, game.settings.IMAGE_SCALE_SHIP))
        self.rect = self.image.get_rect()

        # Start the ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flags
        self.moving_right = False
        self.moving_left = False



    def blitme(self) -> None:
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)



    def update_pos(self) -> None:
        """Update the position, based on the movement flags"""
        if (self.moving_right):
            self.rect.x += 1
        if (self.moving_left):
            self.rect.x -= 1