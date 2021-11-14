import pygame.font


class Button:


    def __init__(self, game, message: str) -> None:
        """Initialise a button"""

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Set dimensions and properties
        self.width, self.height = 200, 50
        self.button_colour = (20, 180, 20)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Create the buttons rectangle and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._set_message(message)



    def draw_button(self):
        """Draw the button and its message"""
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)





    def _set_message(self, message: str):
        """Set the message to be displayed on the button"""
        self.msg_image = self.font.render(message, True, self.text_colour, self.button_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    


