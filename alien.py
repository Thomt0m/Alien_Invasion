import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """An alien ship entity"""


    def __init__(self, game, size) -> None:
        """Initialise the alien ship"""
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings.alien

        # Load the ship image and set its rectangle attributes
        self.image = pygame.image.load("Assets/AlienShip01.png")
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()

        # set the starting location, top left of screen
        self.rect.x = self.rect.width * self.settings.edge_margin_hor
        self.rect.y = self.rect.height * self.settings.edge_margin_vert

        # Movement, in pixels per frame
        self.speed_x = game.settings.screen.width * self.settings.speed_hor_multiplier
        


    def set_initial_pos(self, x, y):
        """Set the initial position of the alien. Copies given positions over to x and y floats"""
        self.rect.x = x
        self.x = float(self.rect.x)
        self.rect.y = y
        self.y = float(self.rect.y)



    def update(self):
        """Update the alien ship, eg pos"""
        self.x += self.speed_x * self.settings.fleet_movement_direction
        self.rect.x = self.x