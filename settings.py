class Settings():
    #STORES SETTINGS OF ALIEN INVASION
    def __init__(self):
       self.screen_width=1200
       self.screen_height=800
       self.bg_color=(0,0,0)

       #ship settings
       self.ship_speed_factor=6.1
       self.ship_limit=3

       self.alienSpeedFactor=1
       self.alien_drop_speed=30
       self.fleet_direction=1

       self.bullet_speed_factor=3.8
       self.bullet_width=4
       self.bullet_height=20
       self.bullet_color=255,0,0
       self.bullets_allowed=3
       
