import pygame as pg

class Ship:
    """class to manage ship properties and functions"""
    def __init__(self, display):
        """initialising ship attributes"""
        self.settings = display.settings
        self.screen = display.screen
        self.ship_colour = self.settings.ship_colour
        self.rect = pg.Rect(0, 0, self.settings.ship_width, self.settings.ship_height)
        self.rect.centery = self.screen.get_rect().centery
        self.y = float(self.rect.y)
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """updates position of ship when moved"""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen.get_rect().bottom:
            self.y += self.settings.ship_speed
            
        self.rect.y = self.y
    

    def draw_ship(self):
        """draws ship on screen"""
        pg.draw.rect(self.screen, self.ship_colour, self.rect)
            
