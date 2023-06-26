import pygame
from .page_objects import text_box
from .game import pixel_game_page

# TODO redundancy, eg tap_x and tap_pos_box.x -> listener or in box both

class editor_page:
    def __init__(self, window):
        # window / basics
        self.window = window
        self.width = window.get_width()
        self.height = window.get_height()
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        # list TODO Database reader
        self.types = ["tap", "circle", "star"]
        self.song_list = ["Fresh_Body_Shop", "RED_LIGHT", "Out_Of_My_Head"]
        self.song_dic = {
            "Fresh_Body_Shop": "Fresh_Body_Shop_-_Handcrafted",
            "RED_LIGHT": "RED_LIGHT_-_EGOR_BUDENNYY",
            "Out_Of_My_Head": "Tom_Orlando_-_Out_Of_My_Head_[Radio_Edit]",
        }

        # on keyboard press change
        self.star_move = "pos"
        self.tap_move = "pos"
        self.circle_move = "startcircle"

        # game window
        self.game_x = self.width*0.05
        self.game_y = self.height*0.275
        self.game_width = self.width * 0.55
        self.game_height = self.height * 0.55
        self.game = pixel_game_page(window, self.game_x, self.game_y, 
                    self.game_width, self.game_height)

        self.color1 = (0, 0, 255)
        self.color2 = (0, 0, 128)

        # tap settings
        self.tap_color1 = (0, 0, 255)
        self.tap_color2 = (0, 0, 128)
        self.tap_x = 275
        self.tap_y = 275
        self.duration = 30

        # circle settings
        self.circle_color1 = (0, 0, 255)
        self.circle_color2 = (0, 0, 128)
        self.travel_speed = 30
        self.hold_length = 0
        self.startcircle = 1

        # star settings
        self.star_color1 = (0, 0, 255)
        self.star_color2 = (0, 0, 128)
        self.star_x = 275
        self.star_y = 275
        self.startcircle1 = 1
        self.startcircle2 = 2

        # color dictionaries
        self.color_dic = {
            "tap": (self.tap_color1, self.tap_color2), 
            "circle": (self.circle_color1, self.circle_color2), 
            "star": (self.star_color1, self.star_color2)
        }

        # text center position
        self.headline_pos   = (self.width*0.50, self.height*0.075)

        # box info
        self.boundary_inner_width = 3
        self.boundary_color = (128, 0, 128)

        # headline
        self.headline = text_box(window, "Editor", self.width*0.5, self.height*0.075, 
                    self.width * 0, self.height * 0)

        # left side 
        self.back_box = text_box(window, "<--", self.width*0.8, self.height*0.117, 
                            self.width * 0.06, self.height * 0.06)
        
        self.fsel_box = text_box(window, "file selector", self.width*0.15, self.height*0.200, 
                            self.width * 0.300, self.height * 0.05)
        
        self.plus_box = text_box(window, "+", self.width*0.45, self.height*0.2, 
                            self.width * 0.05, self.height * 0.05)

        self.trash_box = text_box(window, "trash", self.width*0.05, self.height*0.9, 
                            self.width * 0.1, self.height * 0.05)

        self.game_box = text_box(window, "", self.width*0.05, self.height*0.275, 
                    self.width * 0.55, self.height * 0.55)

        # right side
        self.ssel_box = text_box(window, self.song_list[0], self.width*0.7, self.height*0.2, 
            self.width * 0.2, self.height * 0.05,
            font=pygame.font.Font('freesansbold.ttf', 
                    int(self.width * 0.2/len(self.song_list[0])+6)))
        
        self.ssel_l_box = text_box(window, "<", self.width*0.65, self.height*0.2, 
                            self.width * 0.05, self.height * 0.05)
        
        self.ssel_r_box = text_box(window, ">", self.width*0.9, self.height*0.2, 
                            self.width * 0.05, self.height * 0.05)
        
        self.srew_box = text_box(window, "song rewinder", self.width*0.65, self.height*0.25, 
                            self.width * 0.3, self.height * 0.05)
        
        self.mrew_box = text_box(window, "manual rewinder", self.width*0.65, self.height*0.3, 
                            self.width * 0.3, self.height * 0.05)
        
        self.play_box = text_box(window, "Play", self.width*0.75, self.height*0.35, 
                    self.width * 0.100, self.height * 0.05)
        
        self.type_box = text_box(window, self.types[0], self.width*0.7, self.height*0.45, 
                            self.width * 0.2, self.height * 0.05)
        
        self.type_l_box = text_box(window, "<", self.width*0.65, self.height*0.45, 
                            self.width * 0.05, self.height * 0.05)
        
        self.type_r_box = text_box(window, ">", self.width*0.9, self.height*0.45, 
                            self.width * 0.05, self.height * 0.05)
        
        self.save_box = text_box(window, "save", self.width*0.65, self.height*0.9, 
                            self.width * 0.3, self.height * 0.05)

        self.color1_box = text_box(window, self.color1, self.width*0.65, self.height*0.5, 
                            self.width * 0.3, self.height * 0.05)
        self.color2_box = text_box(window, self.color2, self.width*0.65, self.height*0.55, 
                                   self.width * 0.3, self.height * 0.05)

        self.reset_box = text_box(window, "reset", self.width*0.65, self.height*0.7, 
                            self.width * 0.3, self.height * 0.05)

        self.boxes =[self.fsel_box, self.plus_box, 
                     self.trash_box, 
                     self.ssel_box, self.ssel_l_box, self.ssel_r_box, 
                     self.srew_box, self.mrew_box, 
                     self.type_box, self.type_l_box, self.type_r_box, self.play_box,
                     self.save_box,
                     self.color1_box, self.color2_box,
                     self.reset_box]

        # circle settings
        self.startcircle_box = text_box(window, self.startcircle, self.width*0.65, self.height*0.6, 
                            self.width * 0.3, self.height * 0.05)
        self.circle_hold_box = text_box(window, self.hold_length, self.width*0.65, self.height*0.65, 
                            self.width * 0.3, self.height * 0.05)
        self.circle_setting_boxes = [self.startcircle_box, self.circle_hold_box]
        
        # tap settings
        self.tap_pos_box = text_box(window, (self.tap_x, self.tap_y), self.width*0.65, self.height*0.6, 
                            self.width * 0.3, self.height * 0.05)
        self.tap_hold_box = text_box(window, self.hold_length, self.width*0.65, self.height*0.65, 
                            self.width * 0.3, self.height * 0.05)
        self.tap_setting_boxes = [self.tap_pos_box, self.tap_hold_box]
        
        # star settings
        self.startcircle1_box = text_box(window, self.startcircle1, self.width*0.65, self.height*0.6, 
                            self.width * 0.15, self.height * 0.05)
        self.startcircle2_box = text_box(window, self.startcircle2, self.width*0.8, self.height*0.6, 
                            self.width * 0.15, self.height * 0.05)
        self.star_pos_box = text_box(window, (self.star_x, self.star_y), self.width*0.65, self.height*0.65, 
                            self.width * 0.3, self.height * 0.05)
        self.star_setting_boxes = [self.startcircle1_box, self.startcircle2_box,
                                   self.star_pos_box]

        self.type_dic = {
            "tap": self.tap_setting_boxes, 
            "circle": self.circle_setting_boxes, 
            "star": self.star_setting_boxes
        }

    # TODO clean up
    def move_up(self):
        if self.types[0] == "circle": pass
        if self.types[0] == "tap": 
            if self.tap_move == "pos": self.tap_y -= 10
            if self.tap_move == "hold": self.duration += 5
        if self.types[0] == "star": 
            if self.star_move == "pos": self.star_y -= 10
        self.draw()

    def move_right(self):
        if self.types[0] == "circle": 
            if self.circle_move == "startcircle": self.startcircle = (self.startcircle+1)%8
            # TODO if self.circle_move == "hold": self.duration += 5
        if self.types[0] == "tap":
            if self.tap_move == "pos": self.tap_x += 10
            if self.tap_move == "hold": self.duration += 5
        if self.types[0] == "star": 
            if self.star_move == "pos": self.star_x += 10
            if self.star_move == "startcircle1": self.startcircle1 = (self.startcircle1+1)%8
            if self.star_move == "startcircle2": self.startcircle2 = (self.startcircle2+1)%8
        self.draw()

    def move_down(self):
        if self.types[0] == "circle": pass
        if self.types[0] == "tap": 
            if self.tap_move == "pos": self.tap_y += 10
            if self.tap_move == "hold": self.duration = max(0, self.duration -5)
        if self.types[0] == "star": 
            if self.star_move == "pos":self.star_y += 10
        self.draw()

    def move_left(self):
        if self.types[0] == "circle": 
            if self.circle_move == "startcircle": self.startcircle = (self.startcircle-1)%8
            # TODO if self.circle_move == "hold": self.duration -= 5
        if self.types[0] == "tap": 
            if self.tap_move == "pos": self.tap_x -= 10
            if self.tap_move == "hold": self.duration = max(0, self.duration -5)
        if self.types[0] == "star": 
            if self.star_move == "pos": self.star_x -= 10
            if self.star_move == "startcircle1": self.startcircle1 = (self.startcircle1-1)%8
            if self.star_move == "startcircle2": self.startcircle2 = (self.startcircle2-1)%8
        self.draw()

    def draw(self):
        self.window.fill((0, 0, 0))
        pygame.font.init()

        # headline
        self.headline.draw_text()
        self.back_box.draw_circle_with_text()
        self.game_box.draw_rect()

        # general setttings
        for box in self.boxes:
            box.draw_rect_with_text()

        # type specific settings
        for box in self.type_dic[self.types[0]]:
            box.draw_rect_with_text()

        # game screen
        self.game.draw()
        if self.types[0] == "circle": 
            self.game.draw_prev_circle(self.startcircle, self.hold_length, 
                                self.circle_color1, self.circle_color2)
    
        if self.types[0] == "tap":
            # TODO listener ? sonst muss bei jeder Änderung agepasst werden
            self.tap_pos_box.text = (self.tap_x, self.tap_y)
            self.game.draw_prev_tap(self.tap_x + self.game_x, self.tap_y + self.game_y, 
                                self.duration, 
                                self.tap_color1, self.tap_color2)
        
        if self.types[0] == "star":  
             self.star_pos_box.text = (self.star_x, self.star_y)
             self.game.draw_prev_star(self.startcircle1, self.startcircle2, 
                                self.star_x + self.game_x, self.star_y + self.game_y, 
                                self.star_color1, self.star_color2)

    def click(self, x, y):
        # previous type
        if self.type_l_box.x <= x <= self.type_l_box.x + self.type_l_box.width and \
                self.type_l_box.y <= y <= self.type_l_box.y + self.type_l_box.height:
            new_type = self.types[-1]
            self.types.remove(new_type)
            self.types.insert(0, new_type)
            self.type_box.text = new_type
            self.color1, self.color2 = self.color_dic[self.types[0]]
        
        # next type
        if self.type_r_box.x <= x <= self.type_r_box.x + self.type_r_box.width and \
                self.type_r_box.y <= y <= self.type_r_box.y + self.type_r_box.height:
            cur_type = self.types[0]
            self.types.remove(cur_type)
            self.types.append(cur_type)
            self.type_box.text = self.types[0]
            self.color1, self.color2 = self.color_dic[self.types[0]]

        # type creation
        if self.type_box.x <= x <= self.type_box.x + self.type_box.width and \
                self.type_box.y <= y <= self.type_box.y + self.type_box.height:
            if self.types[0] == "tap":
                self.game.add_tap(self.tap_x + self.game_x, self.tap_y + self.game_y, 
                                    self.duration, self.tap_color1, self.tap_color2)
            if self.types[0] == "circle":
                self.game.add_circle(self.startcircle, self.hold_length, 
                                    self.circle_color1, self.circle_color2)
            if self.types[0] == "star":
                self.game.add_star(self.startcircle1, self.startcircle2,
                                   self.star_x + self.game_x, self.star_y + self.game_y,
                                   self.star_color1, self.star_color2)

        # color1 change
        if self.color1_box.x <= x <= self.color1_box.x + self.color1_box.width and \
                self.color1_box.y <= y <= self.color1_box.y + self.color1_box.height:
            print("color1")
            
        # color2 change
        if self.color2_box.x <= x <= self.color2_box.x + self.color2_box.width and \
                self.color2_box.y <= y <= self.color2_box.y + self.color2_box.height:
            print("color2")

        # circle settings
        if self.startcircle_box.x <= x <= self.startcircle_box.x + self.startcircle_box.width and \
                self.startcircle_box.y <= y <= self.startcircle_box.y + self.startcircle_box.height:
             self.circle_move = "startcircle"

        if self.circle_hold_box.x <= x <= self.circle_hold_box.x + self.circle_hold_box.width and \
                self.circle_hold_box.y <= y <= self.circle_hold_box.y + self.circle_hold_box.height:
             self.circle_move = "hold"

        # tap settings
        if self.tap_pos_box.x <= x <= self.tap_pos_box.x + self.tap_pos_box.width and \
                self.tap_pos_box.y <= y <= self.tap_pos_box.y + self.tap_pos_box.height:
             self.tap_move = "pos"

        if self.tap_hold_box.x <= x <= self.tap_hold_box.x + self.tap_hold_box.width and \
                self.tap_hold_box.y <= y <= self.tap_hold_box.y + self.tap_hold_box.height:
             self.tap_move = "hold"

        # star settings
        if self.startcircle1_box.x <= x <= self.startcircle1_box.x + self.startcircle1_box.width and \
                self.startcircle1_box.y <= y <= self.startcircle1_box.y + self.startcircle1_box.height:
             self.star_move = "startcircle1"

        if self.startcircle2_box.x <= x <= self.startcircle2_box.x + self.startcircle2_box.width and \
                self.startcircle2_box.y <= y <= self.startcircle2_box.y + self.startcircle2_box.height:
             self.star_move = "startcircle2"

        if self.star_pos_box.x <= x <= self.star_pos_box.x + self.star_pos_box.width and \
                self.star_pos_box.y <= y <= self.star_pos_box.y + self.star_pos_box.height:
             self.star_move = "pos"


        # previous selector
        if self.ssel_l_box.x <= x <= self.ssel_l_box.x + self.ssel_l_box.width and \
                self.ssel_l_box.y <= y <= self.ssel_l_box.y + self.ssel_l_box.height:
                    pygame.mixer.music.stop()
                    self.play_box.text = "Play"
                    song = self.song_list[-1]
                    self.song_list.remove(song)
                    self.song_list.insert(0,song)
                    self.ssel_box.text = self.song_list[0]
                    self.ssel_box.font=pygame.font.Font('freesansbold.ttf', 
                                    int(self.ssel_box.width/len(self.song_list[0])+6))
            
        # next selector
        if self.ssel_r_box.x <= x <= self.ssel_r_box.x + self.ssel_r_box.width and \
                self.ssel_r_box.y <= y <= self.ssel_r_box.y + self.ssel_r_box.height:
                    pygame.mixer.music.stop()
                    self.play_box.text = "Play"
                    song = self.song_list[0]
                    self.song_list.remove(song)
                    self.song_list.append(song)
                    self.ssel_box.text = self.song_list[0]
                    self.ssel_box.font=pygame.font.Font('freesansbold.ttf', 
                                    int(self.ssel_box.width/len(self.song_list[0])+6))

        # reset button
        if self.reset_box.x <= x <= self.reset_box.x + self.reset_box.width and \
                self.reset_box.y <= y <= self.reset_box.y + self.reset_box.height:
            if self.types[0] == "tap":
                self.tap_color1 = (0, 0, 255)
                self.tap_color2 = (0, 0, 128)
                self.tap_x = 275
                self.tap_y = 275
                self.duration = 30

            elif self.types[0] == "circle":
                self.circle_color1 = (0, 0, 255)
                self.circle_color2 = (0, 0, 128)
                self.travel_speed = 30
                self.hold_length = 0
                self.startcircle = 1

            elif self.types[0] == "star":
                self.star_color1 = (0, 0, 255)
                self.star_color2 = (0, 0, 128)
                self.star_x = 275
                self.star_y = 275
                self.startcircle1 = 1
                self.startcircle2 = 2

        # play button
        if self.play_box.x <= x <= self.play_box.x + self.play_box.width and \
                self.play_box.y <= y <= self.play_box.y + self.play_box.height:
            if self.play_box.text == "Play":
                pygame.mixer.music.load("music/" + self.song_dic[self.song_list[0]] + ".mp3")
                pygame.mixer.music.play()
                self.play_box.text = "Halt"
            else:
                pygame.mixer.music.stop()
                self.play_box.text = "Play"

        # trash button
        if self.trash_box.x <= x <= self.trash_box.x + self.trash_box.width and \
                self.trash_box.y <= y <= self.trash_box.y + self.trash_box.height:
            self.game.reset()

        # back
        if self.back_box.x <= x <= self.back_box.x + self.back_box.width and \
                self.back_box.y <= y <= self.back_box.y + self.back_box.width:
            return "start"
        
        self.draw()
        return "editor"