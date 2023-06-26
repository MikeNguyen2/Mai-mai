import pygame

class account_page:
    def __init__(self, window):
        self.window = window
        self.width = window.get_width()
        self.height = window.get_height()
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        # back box
        self.box_width = self.width*0.300
        self.box_height = self.height*0.055
        self.box_margin = 0
        self.back_radius = self.width * 0.03
        self.box_start_x = self.width*0.200
        self.box_start_y = self.height*0.125
        self.back_x = self.box_start_x + 2 * self.box_width
        self.back_y = self.box_start_y - self.height * 0.08
        self.boundary_color = (128, 0, 128)

        self.back_pos = (self.box_start_x + 2 * self.box_width + self.width*0.030, 
                        self.box_start_y - self.height * 0.050)
    
    def draw(self):
        self.window.fill((0, 0, 0))
        pygame.font.init()

        text = self.font.render("<--", True, (0,255,255))
        textRect = text.get_rect()
        textRect.center = self.back_pos
        self.window.blit(text, textRect)
        pygame.draw.circle(self.window, self.boundary_color, self.back_pos, 30, 5)
    
    def click(self, x, y):
        if self.back_x <= x <= self.back_x + self.back_radius*2 and \
                self.back_y <= y <= self.back_y + self.back_radius*2:
            return "start"
        
        return "account"