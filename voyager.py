import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class Voyager:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        
        self.settings = Settings()

        self._set_up_screen()
        pygame.display.set_caption("Voyager")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()

            self._update_bullets()
            
            self._update_screen()

    def _update_bullets(self):
        """Update bullets positions and remove old ones."""
        # update bullets' positions
        self.bullets.update()
        
        # remove bullets that are out of boundary
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            
    def _check_keydown_events(self, event):
        """Respond to keydown events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_f:
            self.settings.full_screen_mode = self.settings.full_screen_mode == False
            self._set_up_screen()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _set_up_screen(self):
        """Set up the game canvas screen, full screen or not depending on the setting"""
        if self.settings.full_screen_mode:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode(
        (self.settings.screen_width, self.settings.screen_height))
    
    def _check_keyup_events(self, event):
        """Respond to keyup events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add to the bullets group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)            
        
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    
if __name__ == '__main__':
    # Make a game instance, and run the game.
    voyager = Voyager()
    voyager.run_game()