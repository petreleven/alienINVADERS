import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        #SET SHIP TO INITIAL POSITION
        self.screen=screen
        self.ai_settings=ai_settings
        #LOAD THE SHIP IMAGE AND OBTAIN ITS RECT
        self.image=pygame.image.load('C:\\Users\\peter\Desktop\\alieninvasion\\images\\Shhip.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #PLACE ship at bottom centre of screen
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        #deccimal values of the ships centre position
        self.center=float( self.rect.centerx)

        #movement  flag
        self.moving_right=False
        self.moving_left=False
    
    def update(self):
        #chnge position if flag is true
        if self.moving_right  and self.rect.right < self.screen_rect.right:
            self.center +=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -=self.ai_settings.ship_speed_factor

        self.rect.centerx=self.center
        
    def center_ship(self):
        self.centerx=self.screen_rect.centerx


    def blitme(self):
        #DRAW THE SHIP
        self.screen.blit(self.image,self.rect)
