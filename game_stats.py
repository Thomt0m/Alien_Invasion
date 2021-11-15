class GameStats:
    """Track the statistics for Alien Invasion"""




    def __init__(self, game) -> None:
        """Initialise statistics"""
        self.settings = game.settings
        self.reset_stats()
        self.game_active = False

        self.highscore = 0






    def reset_stats(self):
        """Reset the statistics"""
        self.lives = self.settings.ship.max_lives
        self.score = 0
        self.level = 1