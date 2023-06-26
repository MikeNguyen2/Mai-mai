import pygame

class text_box:
    def __init__(self, window, text="", x=0, y=0, width=0, height=0, \
                font=pygame.font.Font('freesansbold.ttf', 32), \
                boundary_color=(128, 0, 128), boundary_inner_width=3):
        self.window = window
        self.text = text
        self.font = font
        self.boundary_color = boundary_color
        self.boundary_inner_width = boundary_inner_width

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.center = (self.x + 0.5 * self.width, self.y + 0.5 * self.height)

    def draw_rect_with_text(self):
        self.draw_rect()
        self.draw_text()

    def draw_circle_with_text(self):
        self.draw_circ()
        self.draw_text()

    def draw_rect(self):
        pygame.draw.rect(
                self.window, 
                self.boundary_color, 
                pygame.Rect(
                    self.x, 
                    self.y, 
                    self.width, 
                    self.height),
                    self.boundary_inner_width)

    def draw_text(self):
        text = str(self.text)
        txt = self.font.render(text, True, (0,255,255))
        textRect = txt.get_rect()
        textRect.center = self.center
        self.window.blit(txt, textRect)

    def draw_circ(self):
        pygame.draw.circle(self.window, self.boundary_color, self.center, 30, 5)