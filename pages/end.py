import pygame

class end_page:
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.width = window.get_width()
        self.height = window.get_height()
        self.boundary_color = (128, 0, 128)

        # text positions
        self.headline_pos = (self.width*0.5, self.height*0.375)
        self.again_pos = (self.width*0.25, self.height*0.55)
        self.menu_pos = (self.width*0.75, self.height*0.55)
        self.menu_pos1 = (self.width*0.75, self.height*0.55-self.height*0.015)
        self.menu_pos2 = (self.width*0.75, self.height*0.55+self.height*0.015)

        # again button
        self.again_radius = self.width*0.08
        self.again_start_x = self.width*0.25 - self.again_radius
        self.again_start_y = self.height*0.55 - self.again_radius

        # main menu button
        self.start_radius = self.width*0.080
        self.start_start_x = self.width*0.75 - self.start_radius
        self.start_start_y = self.height*0.55 - self.start_radius

    def draw(self):
        # reset the page
        self.window.fill((0, 0, 0))
        pygame.font.init()

        # draw headline
        text = self.font.render("Finished", True, (0,255,255))
        textRect = text.get_rect()
        textRect.center = self.headline_pos
        self.window.blit(text, textRect)

        # again button
        text = self.font.render("Again", True, (0,255,255))
        textRect = text.get_rect()
        textRect.center = self.again_pos
        self.window.blit(text, textRect)
        pygame.draw.circle(self.window, self.boundary_color, self.again_pos, 80, 5)

        # main menu button
        text = self.font.render("Main", True, (0,255,255))
        textRect = text.get_rect()
        textRect.center = self.menu_pos1
        self.window.blit(text, textRect)

        text = self.font.render("Menu", True, (0,255,255))
        textRect = text.get_rect()
        textRect.center = self.menu_pos2
        self.window.blit(text, textRect)
        pygame.draw.circle(self.window, self.boundary_color, self.menu_pos, 80, 5)

    def click(self, x, y):
        # if clicked on again
        if self.again_start_x <= x <= self.again_start_x + self.again_radius*2 and \
                self.again_start_y <= y <= self.again_start_y + self.again_radius*2:
            pygame.mixer.music.pause()
            return "song selection"
        
        # if clicked on main menu
        if self.start_start_x <= x <= self.start_start_x + self.start_radius*2 and \
                self.start_start_y <= y <= self.start_start_y + self.start_radius*2:
            return "start"

        return "end"