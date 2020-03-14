class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230) # light grey
        self.full_screen_mode = False

        # voyager ship setting
        self.ship_speed = 20
        ## every player has 3 lives/ships before game over
        self.ship_limit = 3 

        # bullet setting
        self.bullet_speed = 30
        self.bullet_width = 300 # 3, 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # alien settings
        self.fleet_drop_speed = 20 # 10
        self.alien_speed = 10.0 # 1.0
        self.fleet_direction = 1 # 1 for moving right, -1 for moving left
        