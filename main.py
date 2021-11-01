import pygame

from ship import Ship
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
    #INITIALIZE GAME AND CREATE SCREEN OBJECT
    pygame.init()
    ai_settings=Settings()

    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship=Ship(ai_settings,screen)
    aliens=Group()
    gf.create_fleet(ai_settings,screen,aliens,ship)
    bullets=Group()

    stats=GameStats(ai_settings)
    #STATRT MAIN GAME LOOP
    while True:
        #WATCH FOR KEYBOARD AND MOUSE EVENTS
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
        gf.update_aliens(stats,screen,ship,bullets,ai_settings,aliens)
        #DRAW SCEEN IN EACH LOOP PASS AND DISPLAY MOST RECENT SCREEN
        gf.update_screen(ai_settings,screen,ship,bullets,aliens)
        


run_game()
