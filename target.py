import pygame as pg

class Target:
    """class to manage target properties and functions"""
    def __init__(self, display):
        """initialising target attributes"""
        self.screen = display.screen
        self.settings = display.settings
        self.target_colour = self.settings.target_colour
        self.rect = pg.Rect(0, 0, self.settings.target_width, self.settings.target_height)
        self.rect.midright = self.screen.get_rect().midright
        self.y = float(self.rect.y)

    
    def update(self):
        """moving target up and down on screen"""
        if self.rect.top <= 0 or self.rect.bottom >= self.screen.get_rect().bottom:
            #changing direction if it touches edges
            self.settings.target_speed *= -1
        self.y += self.settings.target_speed
        self.rect.y = self.y

    
    def draw_target(self):
        """draws target on screen"""
        pg.draw.rect(self.screen, self.target_colour, self.rect)