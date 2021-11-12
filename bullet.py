import pygame
from pygame.sprite import Sprite




class Bullet(Sprite):
    """Basic bullet fired from an enitity"""




    def __init__(self, game) -> None:
        """Create a new bullet object, at the entities current position"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Create the bullet
        self.colour = self.settings.bullet_colour
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop

        # Store the bullet's vertical pos as float
        self.y = float(self.rect.y)






    def update(self) -> None:
        """
        Update the state of the bullet, eg position.
        Gets called from pygame.sprite.group, group.update(), which tries to call a function named update() on each of its elements
        """

        # Update vertical position
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y


    def draw_bullet(self) -> None:
        """Draw bullet to screen"""
        pygame.draw.rect(self.screen, self.colour, self.rect)


