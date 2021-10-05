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

        self.target_colour = (0, 0, 255)
        self.target_width = 10
        self.target_height = 40
        self.target_speed = 1
