from os import path
class Game_Stats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.Game_Active = False
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
