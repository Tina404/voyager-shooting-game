import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, game):
        """Initialize the ship and set its starting position."""
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/voyager.png') # 330 x 240 
        self.image = pygame.transform.scale(self.image, (33, 24))
        self.rect = self.image.get_rect()
        
        # Movement flag added to enable contineous movement
        self.moving_right = False
        self.moving_left = False

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # add this position variable because self.rect.x only accept 
        # integer part of the number assigned to it
        self.x = float(self.rect.x)



    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value, not the rect
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        
        # Update rect object from self.x
        self.rect.x = self.x

        self._check_boundary()

    def _check_boundary(self):
        """boundery check"""
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right
            self.x = self.rect.x
        elif self.rect.left < 0:
            self.rect.left = 0
            self.x = self.rect.x

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)