import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """An alien ship entity"""


    def __init__(self, game, size) -> None:
        """Initialise the alien ship"""
        super().__init__()

        self.screen = game.screen

        # Load the ship image and set its rectangle attributes
        self.image = pygame.image.load("Assets/AlienShip01.png")
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()

        # set the starting location, top left of screen
        self.rect.x = self.rect.width * game.settings.alien_edge_margin_hor
        self.rect.y = self.rect.height * game.settings.alien_edge_margin_vert

        # Store the ships horizontal pos as a float (rect only stores int)
        self.x = float(self.rect.x)