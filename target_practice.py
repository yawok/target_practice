import sys
import pygame as pg
from settings import Settings
from ship import Ship
from target import Target
from bullet import Bullet
from button import Button
from game_stats import GameStats

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
        self.play_button = Button(self, "Play")
        self.stats  = GameStats(self)


    def run(self):
        while True:
            self._check_events()
            if self.stats.game_active:
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
                self._check_play_button(mouse_pos)
                


    def _check_play_button(self, mouse_pos):
        """checks if user has clicked button"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()

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
            self._check_target_hit()
            if bullet.rect.right > self.screen.get_rect().width:
                self.bullets.remove(bullet)
        
    
    def _check_target_hit(self):
        """checks if bullet has hit target"""
        hit_space = self.screen.get_rect().width - 30
        if self.stats.bullets_left > 0:
            for bullet in self.bullets.sprites():
                if bullet.rect.left > hit_space and not pg.sprite.spritecollideany(self.target, self.bullets):
                    self.stats.bullets_left -= 1
        else:
            pg.mouse.set_visible(True)
            self.stats.game_active = False            
 
    
    def _start_game(self):
        """starts game when button is pressed"""
        #resetting game statistics
        self.stats.game_active = True
        self.stats.reset_stats()
        #clearing bullets
        self.bullets.empty()
        #centre ship and target
        self.ship.center_ship()
        self.target.center_target()
        #removing mouse pointer
        pg.mouse.set_visible(False)



    def _update_screen(self):
        """draws screen and its objects"""
        self.screen.fill(self.settings.bg_colour)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.draw_ship()
        self.target.draw_target()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pg.display.flip()
    


if __name__ == "__main__":
    tp = Target_practice()
    tp.run()