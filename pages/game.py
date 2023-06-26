import pygame
import math
from game_objects import circles, taps, stars, circle, star, tap
from generator import generate_tap, generate_circle, generate_star, init_sc, init_sc_by_pixel
import random
from parsers import parse_song
import json
import copy

class game_page:
    def __init__(self, window):
        self.window = window
        self.width = window.get_width()
        self.height = window.get_height()

        self.score = 0
        self.misses = 0
        self.counter = 1

        self.game_background = {
            "center_x": self.width / 2,
            "center_y": self.height / 2,
            "radius_s": self.height * 0.1,
            "radius_l": self.height * 0.5 - self.height*0.05
        }

        self.circles = circles()
        self.stars = stars()
        self.taps = taps()
        self.startcircles = init_sc(window)

        self.file = open("maps/red_light.json")
        self.map_data = json.load(self.file)
        self.timestamps = parse_song(self.map_data)

    def draw(self):
        self.window.fill((0, 0, 0))
        draw_game(self.startcircles, self.game_background, self.window)
        draw_score(self.score, self.misses, self.window)
        draw_circle(self.circles, self.window)
        draw_hold(self.circles, self.window)
        draw_taps(self.taps, self.window)
        draw_star(self.stars, self.window)
        
    def tick(self):
        if(self.counter % 20 == 0):
            hold_bool = random.getrandbits(1)
            hold_time = random.randint(0,3)
            self.circles.add(generate_circle(self.startcircles, hold_bool=hold_bool,hold_time=hold_time))
        if(self.counter % 50 == 0):   
            self.taps.add(generate_tap(self.window))
        if(self.counter % 200 == 0):    
            self.stars.add(generate_star(self.window, self.startcircles))
        self.counter += 1
        circle_miss = self.circles.update()
        tap_miss = self.taps.update()
        star_miss = self.stars.update()
        self.misses = self.misses + circle_miss + tap_miss + star_miss

        # if len(self.timestamps) > 0:
        #     if self.counter == self.timestamps[0]:
        #         datas = self.map_data[str (self.counter)]
        #         self.timestamps.remove(self.timestamps[0])

        #         taps = datas["taps"]
        #         circles = datas["circles"]
        #         stars = datas["stars"]

        #         for i in range(len(taps)):
        #             tap_data = taps[str(i)]
        #             tap_obj = tap(tap_data['x'], tap_data['y'], 
        #                           eval(tap_data['color1']), eval(tap_data['color2']))
        #             tap_obj.timer = tap_data['end']
        #             self.taps.add(tap_obj)

        #         for i in range(len(circles)):
        #             circle_data = circles[str(i)]
        #             circ_obj = copy.copy(self.startcircles[circle_data['startcircle']])
        #             # TODO speed
        #             # time = data.end - self.counter
        #             # circ.speed = 
        #             circ_obj.hold_length = circle_data['hold_length']
        #             self.circles.add(circ_obj)
            
        #         for i in range(len(stars)):
        #             star_data = stars[str(i)]
        #             circ1 = copy.copy(self.startcircles[star_data['startcircle1']])
        #             circ2 = copy.copy(self.startcircles[star_data['startcircle2']])

        #             rotation = math.radians(random.randint(0,359))
        #             radius = self.width/2 - self.width/20.0 - 40

        #             e_x = radius * math.cos(rotation) + self.width/2
        #             e_y = radius * math.sin(rotation) + self.height/2 

        #             m_x = self.width/2  + random.randint(0,100)*((e_x-(self.width/2 )) /100.0)
        #             m_y = self.height/2 + random.randint(0,100)*((e_y-(self.height/2)) /100.0)

        #             x = self.width/2
        #             y = self.height/2

        #             star_obj = star(x, y, circ1.e_x, circ1.e_y, 
        #                         m_x, m_y, circ2.e_x, circ2.e_y, 
        #                         self.width/2, self.height/2,
        #                         (0, 0, 255), (0, 0, 147))
        #             self.stars.add(star_obj)
        #     self.draw()
        #     return "game"
        # else: return "end"
        self.draw()
        return "game"
        
    """
    Click function of the game
    Used by keys (at fixed positions) and mouse

    CIRCLE: is the mouse on the object? -> was it already scored (for hold circles)? -> score -> is hold over? -> score
    TAP: is the mouse on the object? -> score
    STAR: is the mouse on the object? -> which checkpoint are we at ? -> is the mouse on the cp? -> score, check cp

    TODO
    Currently checks every Element. Performance boost possible.
    STAR: not very beautiful solution
    CIRCLE: only first and last click matter
    """
    def click(self, x, y):
        circle_score = self.circles.check_for_points(x, y)
        tap_score = self.taps.check_for_points(x, y)
        star_score = self.stars.check_for_points(x, y)
        self.score = self.score + circle_score + tap_score + star_score
        return "game"

    def reset(self):
        self.circles = circles()
        self.taps = taps()
        self.stars = stars()
        self.misses = 0
        self.score = 0
        self.counter = 1
        self.timestamps = parse_song(self.map_data)

    def generate_star(self): self.stars.add(generate_star(self.window, self.startcircles))
    def generate_tap(self): self.taps.add(generate_tap(self.window))
    def generate_circle(self): self.circles.add(generate_circle(self.startcircles))



"""
Draw the basic Outlay
black background
pink outer circle
pink inner circle
usable keys
scoreboard
"""
def draw_game(startcircles, game_background, window):
    pygame.draw.circle(window, (255, 0, 255), (game_background['center_x'], game_background['center_y']), game_background['radius_s'],3)
    pygame.draw.circle(window, (255, 0, 255), (game_background['center_x'], game_background['center_y']), game_background['radius_l'],6)
    keys = ["q","w","e","r","a","s","d","f"]
    for i in range(8):
        key = keys[i]
        circle = startcircles[i]
        font = pygame.font.Font(None, 30)
        score_text = font.render(key, True, (255, 255, 255))
        window.blit(score_text, (circle.e_x, circle.e_y))

"""
Draw the scoreboard
shows the number of hits and misses
"""
def draw_score(score, misses, window):
    font = pygame.font.Font(None, 30)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    width = window.get_width()
    height = window.get_height()
    window.blit(score_text, (width*0.010, height*0.010))

    font = pygame.font.Font(None, 30)
    score_text = font.render("Misses: " + str(misses), True, (255, 255, 255))
    window.blit(score_text, (width-width*0.125, height*0.010)) 


"""
Draw the given circles on the window
The size is dependent on the progress of the way 
"""
def draw_circle(circles, window):
    for circle in circles.get_circles():
        max_length_x = circle.s_x - circle.e_x
        max_length_y = circle.s_y - circle.e_y
        max_length = math.sqrt(math.pow(max_length_x,2) + math.pow(max_length_y, 2))

        cur_length_x = circle.s_x - circle.x
        cur_length_y = circle.s_y - circle.y
        cur_length = math.sqrt(math.pow(cur_length_x,2) + math.pow(cur_length_y, 2))
        pygame.draw.circle(window, circle.color1, (circle.x, circle.y), int(10 * cur_length/max_length)+ window.get_height()*0.02, 150)
        pygame.draw.circle(window, circle.color2, (circle.x, circle.y), int(10 * cur_length/max_length)+ window.get_height()*0.02 + window.get_height()*0.005, 5)

"""
Draw the hold effect for the given circles
The line caps at the inner circle
"""
def draw_hold(circles, window):
    for circle in circles.get_circles():
        if circle.hold_length > 0:
            farthest_length = math.sqrt(math.pow(circle.x-circle.s_x,2) + math.pow(circle.y-circle.s_y, 2))
            length = min(farthest_length, circle.hold_length)
            farthest_length = max(farthest_length,1)
            hold_x = (length/farthest_length) * (circle.x-circle.s_x)
            hold_y = (length/farthest_length) * (circle.y-circle.s_y)
            draw_to =  (int(circle.x-hold_x), int(circle.y-hold_y))
            draw_from = (int(circle.x),  int(circle.y))
            pygame.draw.lines(window, circle.color1, False, (draw_from, draw_to), 35)

"""
Draw the given taps as a 'X'
"""
def draw_taps(taps, window):
    tap_width = 10
    for tap in taps.get_taps():
        pygame.draw.lines(window, tap.color1, False, ((tap.x+3, tap.y+3), (tap.x+tap.radius, tap.y+tap.radius)), tap_width)
        pygame.draw.lines(window, tap.color1, False, ((tap.x+3, tap.y-3), (tap.x+tap.radius, tap.y-tap.radius)), tap_width)
        pygame.draw.lines(window, tap.color1, False, ((tap.x-3, tap.y+3), (tap.x-tap.radius, tap.y+tap.radius)), tap_width)
        pygame.draw.lines(window, tap.color1, False, ((tap.x-3, tap.y-3), (tap.x-tap.radius, tap.y-tap.radius)), tap_width)

"""
draw the star and its line
TODO 
secondary color
line should show the way, then follow the star
"""
def draw_star(stars, window):
    setoff = 5
    for star in stars.get_stars():
        def draw_stripes(start, end , window):
            pygame.draw.lines(window, star.color2, False, (start, end), star.lane_width)  
            a_x = start[0]
            a_y = start[1]
            c_x = end[0]
            c_y = end[1]

            slope_x = a_x - c_x
            slope_y = a_y - c_y

            dir_x = 0
            dir_y = 0
            if slope_x > 0:
                dir_x = 1
            elif slope_x < 0:
                dir_x = -1
            if slope_y > 0:
                dir_y = 1
            elif slope_y < 0:
                dir_y = -1

            steps = 20
            len = 15
            for i in range(0,steps):
                b_x = a_x - slope_x/steps * i + dir_x * len #+ slope_y/25
                b_y = a_y - slope_y/steps * i - dir_y * len #- slope_x/25 
                d_x = a_x - slope_x/steps * i - dir_x * len #- slope_y/25 
                d_y = a_y - slope_y/steps * i + dir_y * len #+ slope_x/25 
                m_x = a_x - slope_x/steps * (i+1)
                m_y = a_y - slope_y/steps * (i+1)
                pygame.draw.lines(window, star.color2, False, ((m_x, m_y), (b_x, b_y)), star.lane_width)  
                pygame.draw.lines(window, star.color2, False, ((m_x, m_y), (d_x, d_y)), star.lane_width)  
        if star.cp2 == False:
            draw_stripes((star.s_x, star.s_y), (star.m_x, star.m_y) , window)
        draw_stripes((star.m_x, star.m_y), (star.e_x, star.e_y) , window)

        point_list = [(star.x+ 0,star.y-20),(star.x+setoff,star.y-setoff),
                      (star.x+15,star.y-10),(star.x+setoff,star.y),
                      (star.x+15,star.y+10),(star.x,star.y+setoff),
                      (star.x-15,star.y+10),(star.x-setoff,star.y),
                      (star.x-20,star.y-10),(star.x-setoff,star.y-setoff),
                      (star.x+ 0,star.y-20),]
        pygame.draw.polygon( window, star.color1, point_list)

class pixel_game_page:
    def __init__(self, window, x, y, width, height):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.score = 0
        self.misses = 0
        self.counter = 0

        self.circles = circles()
        self.stars = stars()
        self.taps = taps()
        self.startcircles = init_sc_by_pixel(x,y,width,height)

        self.game_background = {
            "center_x": self.x + self.width / 2,
            "center_y": self.y + self.height / 2,
            "radius_s": self.height * 0.1,
            "radius_l": self.height * 0.45 - self.height*0.05
        }

        self.file = open("maps/red_light.json")
        self.map_data = json.load(self.file)
        self.timestamps = parse_song(self.map_data)

    def draw(self):
        draw_game(self.startcircles, self.game_background, self.window)
        draw_circle(self.circles, self.window)
        draw_hold(self.circles, self.window)
        draw_taps(self.taps, self.window)
        draw_star(self.stars, self.window)

    def draw_prev_circle(self, pos, hold_length, color1, color2):
        circ_obj = copy.copy(self.startcircles[pos])
        circ_obj.hold_length = hold_length
        circ_obj.color1 = color1
        circ_obj.color2 = color2

        max_length_x = circ_obj.s_x - circ_obj.e_x
        max_length_y = circ_obj.s_y - circ_obj.e_y
        max_length = math.sqrt(math.pow(max_length_x,2) + math.pow(max_length_y, 2))

        cur_length_x = circ_obj.s_x - circ_obj.x
        cur_length_y = circ_obj.s_y - circ_obj.y
        cur_length = math.sqrt(math.pow(cur_length_x,2) + math.pow(cur_length_y, 2))
        pygame.draw.circle(self.window, circ_obj.color1, (circ_obj.x, circ_obj.y), int(10 * cur_length/max_length)+ self.window.get_height()*0.02, 150)
        pygame.draw.circle(self.window, circ_obj.color2, (circ_obj.x, circ_obj.y), int(10 * cur_length/max_length)+ self.window.get_height()*0.02 + self.window.get_height()*0.005, 5)
        
    def draw_prev_tap(self, x, y, timer, color1, color2):
        tap_obj = tap(x, y, color1, color2)
        tap_obj.timer = timer
        tap_width = 10
        pygame.draw.lines(self.window, tap_obj.color1, False, ((tap_obj.x+3, tap_obj.y+3), (tap_obj.x+tap_obj.radius, tap_obj.y+tap_obj.radius)), tap_width)
        pygame.draw.lines(self.window, tap_obj.color1, False, ((tap_obj.x+3, tap_obj.y-3), (tap_obj.x+tap_obj.radius, tap_obj.y-tap_obj.radius)), tap_width)
        pygame.draw.lines(self.window, tap_obj.color1, False, ((tap_obj.x-3, tap_obj.y+3), (tap_obj.x-tap_obj.radius, tap_obj.y+tap_obj.radius)), tap_width)
        pygame.draw.lines(self.window, tap_obj.color1, False, ((tap_obj.x-3, tap_obj.y-3), (tap_obj.x-tap_obj.radius, tap_obj.y-tap_obj.radius)), tap_width)

    def draw_prev_star(self, pos1, pos2, x, y, color1, color2):
        startcircle1 = copy.copy(self.startcircles[pos1])
        startcircle2 = copy.copy(self.startcircles[pos2])
        start_x = self.x + self.width/2
        start_y = self.y + self.height/2
        star_obj = star(start_x, start_y, 
                startcircle1.e_x, startcircle1.e_y, 
                x, y, startcircle2.e_x, startcircle2.e_y, 
                self.width/2, self.height/2,
                (0, 0, 255), (0, 0, 147))
        star_obj.color1 = color1
        star_obj.color2 = color2

        def draw_stripes(start, end , window):
            pygame.draw.lines(window, star_obj.color2, False, (start, end), star_obj.lane_width)  
            a_x = start[0]
            a_y = start[1]
            c_x = end[0]
            c_y = end[1]

            slope_x = a_x - c_x
            slope_y = a_y - c_y

            dir_x = 0
            dir_y = 0
            if slope_x > 0:
                dir_x = 1
            elif slope_x < 0:
                dir_x = -1
            if slope_y > 0:
                dir_y = 1
            elif slope_y < 0:
                dir_y = -1

            steps = 20
            len = 15
            for i in range(0,steps):
                b_x = a_x - slope_x/steps * i + dir_x * len 
                b_y = a_y - slope_y/steps * i - dir_y * len 
                d_x = a_x - slope_x/steps * i - dir_x * len 
                d_y = a_y - slope_y/steps * i + dir_y * len 
                m_x = a_x - slope_x/steps * (i+1)
                m_y = a_y - slope_y/steps * (i+1)
                pygame.draw.lines(self.window, star_obj.color2, False, ((m_x, m_y), (b_x, b_y)), star_obj.lane_width)  
                pygame.draw.lines(self.window, star_obj.color2, False, ((m_x, m_y), (d_x, d_y)), star_obj.lane_width)  
        if star_obj.cp2 == False:
            draw_stripes((star_obj.s_x, star_obj.s_y), (star_obj.m_x, star_obj.m_y) , self.window)
        draw_stripes((star_obj.m_x, star_obj.m_y), (star_obj.e_x, star_obj.e_y) , self.window)
        setoff = 5
        point_list = [(star_obj.x+ 0,star_obj.y-20),(star_obj.x+setoff,star_obj.y-setoff),
                      (star_obj.x+15,star_obj.y-10),(star_obj.x+setoff,star_obj.y),
                      (star_obj.x+15,star_obj.y+10),(star_obj.x,star_obj.y+setoff),
                      (star_obj.x-15,star_obj.y+10),(star_obj.x-setoff,star_obj.y),
                      (star_obj.x-20,star_obj.y-10),(star_obj.x-setoff,star_obj.y-setoff),
                      (star_obj.x+ 0,star_obj.y-20),]
        pygame.draw.polygon( self.window, star_obj.color1, point_list)


    def tick(self):
        self.counter += 1
        circle_miss = self.circles.update()
        tap_miss = self.taps.update()
        star_miss = self.stars.update()
        self.misses = self.misses + circle_miss + tap_miss + star_miss
        return "game"
    
    def add_circle(self, pos, hold_length, color1, color2):
        circ_obj = copy.copy(self.startcircles[pos])
        circ_obj.hold_length = hold_length
        circ_obj.color1 = color1
        circ_obj.color2 = color2
        self.circles.add(circ_obj)

    def add_tap(self, x, y, timer, color1, color2):
        tap_obj = tap(x, y, color1, color2)
        tap_obj.timer = timer
        self.taps.add(tap_obj)

    def add_star(self, pos1, pos2, x, y, color1, color2):
        startcircle1 = copy.copy(self.startcircles[pos1])
        startcircle2 = copy.copy(self.startcircles[pos2])
        start_x = self.x + self.width/2
        start_y = self.y + self.height/2
        star_obj = star(start_x, start_y, 
                startcircle1.e_x, startcircle1.e_y, 
                x, y, startcircle2.e_x, startcircle2.e_y, 
                self.width/2, self.height/2,
                (0, 0, 255), (0, 0, 147))
        star_obj.color1 = color1
        star_obj.color2 = color2
        self.stars.add(star_obj)

    def reset(self):
        self.circles = circles()
        self.taps = taps()
        self.stars = stars()
        self.timestamps = parse_song(self.map_data)