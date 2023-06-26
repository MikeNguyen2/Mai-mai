import pygame

class start_page:
    def __init__(self, window):
        self.window = window
        self.width = window.get_width()
        self.height = window.get_height()

        self.box_width = self.width*0.300
        self.box_height = self.height*0.100
        self.box_margin = self.height*0.050

        self.box_start_x = self.width*0.350
        self.box_start_y = self.height*0.200
        self.box2_start_y = self.box_start_y + self.box_height + self.box_margin
        self.box3_start_y = self.box2_start_y + self.box_height + self.box_margin
        self.box4_start_y = self.box3_start_y + self.box_height + self.box_margin

        self.headline_pos = (self.width*0.5, self.height*0.1)
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.categories = ["Play", "Edit", "Settings", "Account"]
        self.box_color = (128, 128, 128)

    def draw(self):
        # reset the window
        self.window.fill((0, 0, 0))
        pygame.font.init() 

        # draw the categories
        for i in range(len(self.categories)):
            box_y = self.box_start_y + i*self.box_height + i*self.box_margin
    
            pygame.draw.rect(
                self.window, 
                self.box_color, 
                pygame.Rect(
                    self.box_start_x, 
                    box_y, 
                    self.box_width, 
                    self.box_height))
            
            text = self.font.render(self.categories[i], True, (0,255,255))
            textRect = text.get_rect()
            textRect.center = ((2 * self.box_start_x + self.box_width)/2, 
                            (2 * box_y+self.box_height)/2)
            self.window.blit(text, textRect)

            text = self.font.render("MyMai", True, (0,255,255))
            textRect = text.get_rect()
            textRect.center = self.headline_pos
            self.window.blit(text, textRect)

    def click(self, x, y):
        s_x = self.box_start_x
        e_x = s_x + self.box_width

        s_y = self.box_start_y
        e_y = s_y + self.box_height

        s_y2 = e_y + self.box_margin
        e_y2 = s_y2 + self.box_height

        s_y3 = e_y2 + self.box_margin
        e_y3 = s_y3 + self.box_height

        s_y4 = e_y3 + self.box_margin
        e_y4 = s_y4 + self.box_height

        if s_x <= x <= e_x:
            if s_y <= y <= e_y: return "song selection"
            if s_y2 <= y <= e_y2: return "editor"
            if s_y3 <= y <= e_y3: return "settings"
            if s_y4 <= y <= e_y4: return "account"

        return "start"