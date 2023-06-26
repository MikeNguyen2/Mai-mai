import pygame

class song_selection_page:
    def __init__(self, window):
        self.window = window
        self.width = window.get_width()
        self.height = window.get_height()
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.song_list = ["Fresh_Body_Shop_-_Handcrafted", "RED_LIGHT_-_EGOR_BUDENNYY", "Tom_Orlando_-_Out_Of_My_Head_[Radio_Edit]"]

        # Main selection
        self.box_color = (128, 128, 128)
        self.box_width = self.width*0.4
        self.box_height = self.height*0.4
        self.box_start_x = self.width*0.5 - self.box_width*0.5
        self.box_start_y = self.height*0.33
        self.song_name_pos = (self.box_start_x + self.box_width*0.5, self.box_start_y + self.box_height*0.5)

        # Selectors
        self.selector_color = (128, 128, 128)
        self.selector_width = self.width*0.15
        self.selector_height = self.height*0.15
        self.selector_start_x = self.box_start_x - self.selector_width - self.width*0.05 
        self.selector_start_x2 = self.box_start_x + self.box_width + self.width*0.05
        self.selector_start_y = self.box_start_y + self.box_width*0.5 - self.selector_height*0.5 
        self.previous_pos = (self.selector_start_x + self.selector_width/2, self.selector_start_y + self.selector_height/2)
        self.next_pos = (self.selector_start_x2+ self.selector_width/2, self.selector_start_y + self.selector_height/2)

        # Song title
        self.title_x = self.box_start_x + self.box_width/2
        self.title_y = self.box_start_y - self.height*0.05
        self.title_pos = (self.title_x, self.title_y)

        # Song description
        self.description_x = self.box_start_x + self.box_width/2
        self.description_y = self.box_start_y + self.box_height + self.height*0.05
        self.description_pos = (self.description_x, self.description_y)

    def click(self, x, y):
        # main selection
        if self.box_start_x <= x <= self.box_start_x + self.box_width and \
                self.box_start_y <= y <= self.box_start_y + self.box_height:
            pygame.mixer.music.load("music/" + self.song_list[0] + ".mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(loops=0, start=0.0, fade_ms = 0)
            return "game"

        # previous selector
        if self.selector_start_x <= x <= self.selector_start_x + self.selector_width and \
                self.selector_start_y <= y <= self.selector_start_y + self.selector_height:
                    song = self.song_list[-1]
                    self.song_list.remove(song)
                    self.song_list.insert(0,song)
                    self.draw()
            
        # next selector
        if self.selector_start_x2 <= x <= self.selector_start_x2 + self.selector_width and \
                self.selector_start_y <= y <= self.selector_start_y + self.selector_height:
                    song = self.song_list[0]
                    self.song_list.remove(song)
                    self.song_list.append(song)
                    self.draw()
                    
        return "song selection"

    def draw(self):
        self.window.fill((0, 0, 0))
        pygame.font.init()

        # draw headline
        headline_pos = (self.width*0.5, self.height*0.1)
        text = self.font.render("Song Selection", True, (0,255,255))
        textRect = text.get_rect()
        textRect.center = headline_pos
        self.window.blit(text, textRect)

        # main box
        pygame.draw.rect(
            self.window, 
            self.box_color, 
            pygame.Rect(
                self.box_start_x, 
                self.box_start_y, 
                self.box_width, 
                self.box_height))

        text = self.font.render("Song Cover", True, (0,255,255))
        textRect = text.get_rect()
        textRect.center = self.song_name_pos
        self.window.blit(text, textRect)

        # selectors
        pygame.draw.rect(
            self.window, 
            self.selector_color, 
            pygame.Rect(
                self.selector_start_x,
                self.selector_start_y,
                self.selector_width,
                self.selector_height
                ))
        
        pygame.draw.rect(
            self.window, 
            self.selector_color, 
            pygame.Rect(
                self.selector_start_x2,
                self.selector_start_y,
                self.selector_width,
                self.selector_height
                ))
        
        text = self.font.render("next", True, (0,255,255))
        textRect = text.get_rect()
        textRect.center = self.next_pos
        self.window.blit(text, textRect)

        text = self.font.render("previous", True, (0,255,255))
        textRect = text.get_rect()
        textRect.center = self.previous_pos
        self.window.blit(text, textRect)

        # text
        text = self.font.render("Song description", True, (0,255,255))
        textRect = text.get_rect()
        textRect.center = self.description_pos
        self.window.blit(text, textRect)

        text = self.font.render(self.song_list[0], True, (0,255,255))
        textRect = text.get_rect()
        textRect.center = self.title_pos
        self.window.blit(text, textRect)
        