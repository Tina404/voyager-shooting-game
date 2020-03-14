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
        self.fleet_drop_speed = 5 #20 # 10
        self.alien_speed = 5 # 10.0 # 1.0
        self.fleet_direction = 1 # 1 for moving right, -1 for moving left

        # how quickly the game speeds up with game level
        self.speedup_scale = 1.1

        # scoring
        self.alien_points = 50
        self.score_scale = 1.5 # score points increase with level
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 20.0
        self.bullet_speed = 30.0
        self.alien_speed = 5.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
    
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
