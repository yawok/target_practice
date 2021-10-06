class GameStats:
    """class to manage game statistics"""
    def __init__(self, display):
        """initialising game statistics attributes"""
        self.settings = display.settings
        self.game_active = False
        self.reset_stats()
    
    def reset_stats(self):
        """keeps track of game statistics"""
        self.ship_left = self.settings.ship_left