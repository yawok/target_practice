class Settings:
    """class to manage game settings"""
    def __init__(self):
        self.screen_size = (700, 550)
        self.screen_caption = "Target Practice"
        self.bg_colour = (20, 20, 20)

        self.ship_colour = (255, 255, 255)
        self.ship_width = 30
        self.ship_height = 20
        self.ship_speed = 2
        self.ship_left = 3

        self.target_colour = (0, 0, 255)
        self.target_width = 10
        self.target_height = 40
        

        self.bullet_colour = (200, 0, 0)
        self.bullet_width = 30
        self.bullet_height = 20
        self.bullets_allowed = 2
        self.bullet_speed = 1.5
        self.bullets_left = 5

        self.initialising_dynamic_settings()

    def initialising_dynamic_settings(self):
        """Initialising game's dynamic settings."""
        self.target_speed = 1
    
    def increase_speed(self):
        """Increasing target speed"""
        self.target_speed *= 1.1
        
