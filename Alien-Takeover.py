import pygame
from Alien_Takeover.set import Settings
from Alien_Takeover.ship import Ship
from Alien_Takeover import game_functions as gf
from pygame.sprite import Group
from Alien_Takeover.game_stats import Game_Stats
from Alien_Takeover.button import Button
from Alien_Takeover.scoreboard import Scoreboard



def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien_Takeover 1")
    play_button = Button(ai_settings, screen, "Play")


    stats = Game_Stats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)

    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)
        if stats.Game_Active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                             bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button)


run_game()
