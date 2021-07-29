class GameStats():
    """Track Statistics for the game"""
    def __init__(self,ai_settings):
        """Initialize Statistics"""
        self.ai_settings=ai_settings
        self.reset_stats()
        #Starts the game in an inactive stats.
        self.game_active=False
        #High score should never reset
        self.high_score=0
    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left=self.ai_settings.ship_limit
        self.score=0
        self.level=1