import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_function as gf
def run_game():
    #initialize Settings game and create a screen object
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Sky War")
    #Create an instance to store game statistics and creates a scoreboard
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)
    #Make a ship, a group of bullets and a group of aliens
    ship=Ship(ai_settings,screen)
    #Make the play button
    play_button=Button(ai_settings,screen,"Play")
    #Make a group to store bullets in.
    bullets=Group()
    aliens=Group()
    #Create a fleet of alien
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #start the main loop for game
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if(stats.game_active):
            ship.update()
            gf.update_bullets(ai_settings, screen, stats,sb,ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats,sb, ship, aliens, bullets, play_button)
run_game()