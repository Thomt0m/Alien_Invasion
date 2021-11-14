import pygame


class Ship:
    """Player's ship, manages the ship"""


    def __init__(self, game, scale_size) -> None:
        """Initialise a ship, and set its starting position"""

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings.ship

        # Load the ship image and get its rectangle
        self.image = pygame.image.load("Assets/Spaceship01.png")
        self.image = pygame.transform.scale(self.image, (scale_size, scale_size))
        self.rect = self.image.get_rect()

        # Start the ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store the ships horizontal pos as a float (rect only stores int)
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

        


    





    def blit_me(self) -> None:
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)



    def update_pos(self) -> None:
        """Update the position, based on the movement flags"""
        if (self.moving_right and self.rect.right < self.screen_rect.right):
            self.x += self.settings.speed_x
        if (self.moving_left and self.rect.left > self.screen_rect.left):
            self.x -= self.settings.speed_x
        self.rect.x = self.x

    def center_ship(self):
        """Place the ship at the bottom center of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


