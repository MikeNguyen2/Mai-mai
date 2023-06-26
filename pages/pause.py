import pygame

class pause_page:
    def __init__(self, window):
        self.window = window
        self.width = window.get_width()
        self.height = window.get_height()
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        # text center position
        self.headline_pos   = (self.width*0.50, self.height*0.375)
        self.continue_pos   = (self.width*0.25, self.height*0.55)
        self.quit_pos       = (self.width*0.75, self.height*0.55)
        self.boundary_color = (128, 0, 128)

        # continue box
        self.continue_radius    = self.width*0.080
        self.continue_start_x   = self.width*0.25 - self.continue_radius
        self.continue_start_y   = self.height*0.55 - self.continue_radius

        # quit box
        self.quit_radius    = self.width*0.080
        self.quit_start_x   = self.width*0.75 - self.quit_radius
        self.quit_start_y   = self.height*0.55 - self.quit_radius

    def draw(self):
        self.window.fill((0, 0, 0))
        pygame.font.init()

        # draw headline
        text = self.font.render("Pause", True, (0,255,255))
        textRect = text.get_rect()
        textRect.center = self.headline_pos
        self.window.blit(text, textRect)

        # Resume button
        text = self.font.render("Resume", True, (0,255,255))
        textRect = text.get_rect()
        textRect.center = self.continue_pos
        self.window.blit(text, textRect)
        pygame.draw.circle(self.window, self.boundary_color, self.continue_pos, self.width*0.080, 5)

        # Quit button
        text = self.font.render("Quit", True, (0,255,255))
        textRect = text.get_rect()
        textRect.center = self.quit_pos
        self.window.blit(text, textRect)
        pygame.draw.circle(self.window, self.boundary_color, self.quit_pos, self.width*0.080, 5)

    def click(self, x, y):
        if self.continue_start_x <= x <= self.continue_start_x + self.continue_radius*2 and \
                self.continue_start_y <= y <= self.continue_start_y + self.continue_radius*2:
            pygame.mixer.music.unpause()
            return "game"

        if self.quit_start_x <= x <= self.quit_start_x + self.quit_radius*2 and \
                self.quit_start_y <= y <= self.quit_start_y + self.quit_radius*2:
            return "end"

        return "pause"
