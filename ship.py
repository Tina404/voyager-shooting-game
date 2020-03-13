import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, game):
        """Initialize the ship and set its starting position."""
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

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1