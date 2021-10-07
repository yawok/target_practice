import pygame.font

class Button:
    """class to manage button and its properties"""
    def __init__(self, display, msg):
        """initialising button attributes"""
        self.settings = display.settings
        self.screen = display.screen
        self.screen_rect = display.screen.get_rect()
        #setting button dimenstions
        self.width, self.height= 200, 50
        self.button_colour = (255, 255, 255)
        self.font_colour = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        #setting rect and placing in button in middle of screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self._prep_msg(msg)

    
    def _prep_msg(self, msg):
        """creating text image"""
        self.msg_image = self.font.render(msg, True, self.font_colour, self.button_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    
    def draw_button(self):
        """draws button on screen"""
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)