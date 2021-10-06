import sys
import pygame as pg
from settings import Settings
from ship import Ship
from target import Target
from bullet import Bullet

class Target_practice:
    """class to manage game resources"""
    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode(self.settings.screen_size)
        pg.display.set_caption(self.settings.screen_caption)
        self.ship = Ship(self)
        self.target = Target(self)
        self.bullets = pg.sprite.Group()


    def run(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self.target.update()
            self._update_screen()
            

    def _check_events(self):
        """checks for keyboard and mouse inputs"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                pass
                #self._check_play_button()


    def _check_keydown_events(self, event):
        """checks for key presses"""
        if event.key == pg.K_UP or event.key == pg.K_w:
            self.ship.moving_up = True
        elif event.key == pg.K_DOWN or event.key == pg.K_s:
            self.ship.moving_down = True
        elif event.key == pg.K_q or event.key == pg.K_ESCAPE:
            sys.exit()
        elif event.key == pg.K_SPACE:
            self._fire_bullets()
        
            
    def _check_keyup_events(self, event):
        """checks for key presses"""
        if event.key == pg.K_UP or event.key == pg.K_w:
            self.ship.moving_up = False
        if event.key == pg.K_DOWN or event.key == pg.K_s:
            self.ship.moving_down = False


    def _fire_bullets(self):
        """creates bullet and adds it to sprite group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """moves bullet to end of screen and deletes it"""
        self.bullets.update()
        for bullet in self.bullets.sprites():
            if bullet.rect.right > self.screen.get_rect().width:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """draws screen and its objects"""
        self.screen.fill(self.settings.bg_colour)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.draw_ship()
        self.target.draw_target()
        pg.display.flip()
    


if __name__ == "__main__":
    tp = Target_practice()
    tp.run()