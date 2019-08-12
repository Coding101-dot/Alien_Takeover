

# ##########################################################################
# #The settings.py file contains the Settings class. This class only has an#
# #__init__() method, which initializes attributes controlling the game’s ##
# #appearance and the ship’s speed.                                       ##
# ##########################################################################


class Settings:

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 700
        self.background_color = (95, 0, 200)
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 5
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = 150, 00, 00
        self.bullets_allowed = 5
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.ship_limit = 3
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
        self.alien_points = 50
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3

        self.alien_speed_factor = 1

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
