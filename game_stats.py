class GameStats:
    """Track the statistics for Alien Invasion"""




    def __init__(self, game) -> None:
        """Initialise statistics"""
        self.settings = game.settings
        self.reset_stats()
        self.game_active = False






    def reset_stats(self):
        """Reset the statistics"""
        self.ships_left = self.settings.ship.max_lives