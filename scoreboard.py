import pygame.font
from pygame.sprite import Group



class Scoreboard:
    """Stores scoring information"""


    def __init__(self, game) -> None:
        """Initialise a scoreboard"""

        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        self.text_colour = (200, 200, 200)
        self.font = pygame.font.SysFont(None, 32)

        self.score_to_image()
        self.highscore_to_image()
        self.player_lives_to_image()
        self.level_to_image()




    def score_to_image(self):
        """Turn the score into a rendered image"""
        # Render the image
        score_str = "Score: {:,}".format(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_colour)
        # Set its pos, top-left with a margin of 20 pixels
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 20


    def highscore_to_image(self):
        """Turn the highscore into a rendered image"""
        # Render the image
        highscore_str = "Highscore: {:,}".format(self.stats.highscore)
        self.highscore_image = self.font.render(highscore_str, True, self.text_colour)
        # Set its pos, top-right
        self.highscore_rect = self.highscore_image.get_rect()
        self.highscore_rect.right = self.screen_rect.right - 20
        self.highscore_rect.top = self.score_rect.top

    
    def player_lives_to_image(self):
        """Turn the number of lives to player has left into a rendered image"""
        # Render the image
        self.lives_image = self.font.render("Lives: " + str(self.stats.ships_left), True, self.text_colour)
        # Set its pos, bottom-left
        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.left = self.screen_rect.left + 20
        self.lives_rect.bottom = self.screen_rect.bottom - 20


    def level_to_image(self):
        """Turn the current level number into a rendered image"""
        # Render the image
        self.level_image = self.font.render("Level: " + str(self.stats.level), True, self.text_colour)
        # Set its pos, bottom right
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.bottom = self.lives_rect.bottom





    def show_score(self):
        """Draw score to screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highscore_image, self.highscore_rect)
        self.screen.blit(self.lives_image, self.lives_rect)
        self.screen.blit(self.level_image, self.level_rect)
