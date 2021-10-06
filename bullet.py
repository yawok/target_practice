import pygame as pg
from pygame.sprite import Sprite

class Bullet(Sprite):
    """class to managebullet and its functions"""
    def __init__(self, display):
        """initialising bullet attributes"""
        super().__init__()
        self.settings = display.settings
        self.screen = display.screen
        self.bullet_colour = self.settings.bullet_colour
        self.rect = pg.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = display.ship.rect.midright
        self.x = float(self.rect.x)


    def update(self):
        """moves bullet across screen"""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x
    
    
    def draw_bullet(self):
        """draws bullet to screen"""
        pg.draw.rect(self.screen, self.bullet_colour, self.rect)
