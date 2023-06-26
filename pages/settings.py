import pygame

class settings_page:
    def __init__(self, window):
        self.window = window
        self.width = window.get_width()
        self.height = window.get_height()
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        # outer box
        self.box_color = (128, 128, 128)
        self.boundary_color = (128, 0, 128)
        self.boundary_inner_width = 3
        self.boundary_outer_width = 10

        # inner boxes
        self.box_width = self.width*0.300
        self.box_height = self.height*0.055
        self.box_margin = 0
        self.box_start_x = self.width*0.200
        self.box_start_x2 = self.width*0.500
        self.box_start_y = self.height*0.125

        # text 
        self.headline_pos = (self.box_start_x + self.box_width, 
                            self.box_start_y - self.height * 0.050)
        self.back_pos = (self.box_start_x + 2 * self.box_width + self.width*0.030, 
                        self.box_start_y - self.height * 0.050)
        
        # back box
        self.back_radius = self.width * 0.03
        self.back_x = self.box_start_x + 2 * self.box_width
        self.back_y = self.box_start_y - self.height * 0.08

        # setting values
        self.categories = 30 * ["Setting"]
        self.values = 30 * ["value"]
        self.num_rows = 15

    def draw(self):
        self.window.fill((0, 0, 0))
        pygame.font.init()

        # draw headline
        text = self.font.render("Settings", True, (0,255,255))
        textRect = text.get_rect()
        textRect.center = self.headline_pos
        self.window.blit(text, textRect)

        # back button
        text = self.font.render("<--", True, (0,255,255))
        textRect = text.get_rect()
        textRect.center = self.back_pos
        self.window.blit(text, textRect)
        pygame.draw.circle(self.window, self.boundary_color, self.back_pos, 30, 5)

        # inner boxes
        for i in range(self.num_rows):
            box_y = self.box_start_y + i*self.box_height + i*self.box_margin

            # settings
            pygame.draw.rect(
                self.window, 
                self.box_color, 
                pygame.Rect(
                    self.box_start_x, 
                    box_y, 
                    self.box_width, 
                    self.box_height))
            pygame.draw.rect(
                self.window, 
                self.boundary_color, 
                pygame.Rect(
                    self.box_start_x, 
                    box_y, 
                    self.box_width, 
                    self.box_height),
                    self.boundary_inner_width)
            text = self.font.render(self.categories[i], True, (0,255,255))
            textRect = text.get_rect()
            textRect.center = ((2 * self.box_start_x + self.box_width)/2, 
                            (2 * box_y+self.box_height)/2)
            self.window.blit(text, textRect)

            # values
            pygame.draw.rect(
                self.window, 
                self.box_color, 
                pygame.Rect(
                    self.box_start_x2, 
                    box_y, 
                    self.box_width, 
                    self.box_height))
            pygame.draw.rect(
                self.window, 
                self.boundary_color, 
                pygame.Rect(
                    self.box_start_x2, 
                    box_y, 
                    self.box_width, 
                    self.box_height),
                    self.boundary_inner_width)
            text = self.font.render(self.values[i], True, (0,255,255))
            textRect = text.get_rect()
            textRect.center = ((2 * self.box_start_x2 + self.box_width)/2, 
                            (2 * box_y+self.box_height)/2)
            self.window.blit(text, textRect)
        
        # Outer box
        pygame.draw.rect(
            self.window, 
            self.boundary_color, 
            pygame.Rect(
                self.box_start_x, 
                self.box_start_y, 
                self.box_width*2, 
                self.box_height*self.num_rows),
                self.boundary_outer_width)

    def click(self, x, y):
        if self.back_x <= x <= self.back_x + self.back_radius*2 and \
                self.back_y <= y <= self.back_y + self.back_radius*2:
            return "start"
        
        return "settings"
    