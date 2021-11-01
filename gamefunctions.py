from pygame.constants import AUDIO_ALLOW_ANY_CHANGE
from ship import Ship
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from winsound import Beep

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    stats.ships_left-=1

    aliens.empty()
    bullets.empty()
    create_fleet(ai_settings,screen,aliens,ship)
    ship.center_ship()
    Beep(frequency=600,duration=600)
    sleep(1)


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_SPACE:
        fire_bullets(ai_settings,screen,ship,bullets)


def fire_bullets(ai_settings,screen,ship,bullets):
    if len(bullets)<ai_settings.bullets_allowed:
            new_bullet=Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)

def check_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False

def check_events(ai_settings,screen,ship,bullets):
    # #WATCH FOR KEYBOARD AND MOUSE EVENTS
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            
            elif event.type==pygame.KEYDOWN:
                #MOVE TO THE RIGHT and LEFT
                check_keydown_events(event,ai_settings,screen,ship,bullets)

            elif event.type==pygame.KEYUP:
                check_keyup_events(event,ship)
                

def update_screen(ai_settings,screen,ship,bullets,aliens):
    #DRAW IMAGES on SCREEN IN EACH LOOP PASS
    screen.fill(ai_settings.bg_color)
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    aliens.draw(screen)
    #DISPLAY MOST RECENT SCREEN
    pygame.display.flip()


def update_bullets(ai_settings,screen,ship,aliens,bullets):
    bullets.update()
    for bullet in bullets.copy():
            if bullet.rect.bottom<=0:
                bullets.remove(bullet)
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    

    if len(aliens)==0:
        bullets.empty()
        create_fleet(ai_settings,screen,aliens,ship)

def get_number_aliens(ai_settings,alien_width):
    available_space_x=ai_settings.screen_width-2*alien_width
    number_aliens_x=int(available_space_x/(2*alien_width))
    return number_aliens_x


def get_number_rows(ai_settings,alien_height,ship_height):
    available_space_y=ai_settings.screen_height-3*alien_height-ship_height
    number_rows=int(available_space_y/(3*alien_height))
    return number_rows


def create_alien(ai_settings,screen,alien_width,alien_number,aliens,row_number):
    alien=Alien(ai_settings,screen)
    alien.x=alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    aliens.add(alien)

def create_fleet(ai_settings,screen,aliens,ship):
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    number_aliens_x=get_number_aliens(ai_settings,alien_width)
    number_rows=get_number_rows(ai_settings,alien.rect.height,ship.rect.height)
    
    for row_number in range (number_rows):
        for alien_number in range (number_aliens_x):
            create_alien(ai_settings,screen,alien_width,alien_number,aliens,row_number)


def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break


def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.alien_drop_speed
    ai_settings.fleet_direction*=-1


def update_aliens(stats,screen,ship,bullets,ai_settings,aliens):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
