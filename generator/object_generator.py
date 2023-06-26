import random
import math
import copy
from game_objects import circle, tap, star


"""
Generate the start circles
Those are used as guidelines for circles etc.
"""
def init_sc(window):
    startcircles = []
    for i in range(8):
        rotation = math.radians(i * 360/8 + 22.5)
        radius = window.get_height()/10
        s_x = radius * math.cos(rotation) + window.get_width()/2
        s_y = radius * math.sin(rotation) + window.get_height()/2

        rotation = math.radians(i * 360/8 + 22.5)
        radius = window.get_height()/2 - window.get_height()/20.0
        e_x = radius * math.cos(rotation) + window.get_width()/2
        e_y = radius * math.sin(rotation) + window.get_height()/2

        startcircles.append(circle(s_x, s_y, s_x, s_y, e_x, e_y,(255, 0, 255), (255, 147, 255), 20))
    return startcircles

def init_sc_by_pixel(x, y, width, height):
    startcircles = []
    for i in range(8):
        rotation = math.radians(i * 360/8 + 22.5)
        radius = width/10
        s_x = radius * math.cos(rotation) + x+width/2
        s_y = radius * math.sin(rotation) + y+height/2

        rotation = math.radians(i * 360/8 + 22.5)
        radius = height/2 - height/20.0
        e_x = radius * math.cos(rotation) + x+width/2
        e_y = radius * math.sin(rotation) + y+height/2

        startcircles.append(circle(s_x, s_y, s_x, s_y, e_x, e_y,(255, 0, 255), (255, 147, 255), 20))
    return startcircles

"""
Generate 1 tap
Calculates the line between the center and the outer circle.
The tap is placed randomly at its way.
TODO There must be a better way
"""
def generate_tap(window, color1=(0, 0, 255), color2=(0, 0, 147)):
    rotation = math.radians(random.randint(0,359))
    radius = window.get_height()/2 - window.get_height()/20.0 - 15

    e_x = radius * math.cos(rotation) + window.get_width()/2
    e_y = radius * math.sin(rotation) + window.get_height()/2 

    x = window.get_width()/2  + random.randint(0,100)*((e_x-(window.get_width()/2 )) /100.0)
    y = window.get_height()/2 + random.randint(0,100)*((e_y-(window.get_height()/2)) /100.0)

    return tap(x, y, color1, color2)

"""
Uses generate_tap 2 times
return a tuple of the 2 taps
"""
def generate_double_tap(window):
    tap1 = generate_tap(window, (255, 255, 0), (255, 255, 147))
    tap2 = generate_tap(window, (255, 255, 0), (255, 255, 147))
    return (tap1, tap2)

"""
Generate 1 circle
randomly selects 1 of the startcircles
TODO 
while hold is happening in a lane, it should get blocked off
"""
def generate_circle(startcircles, hold_bool=False, hold_time=0,speed=30):
    circ = copy.copy(startcircles[random.randint(0,7)])
    if hold_bool:
        circ.hold_length = 100 + 50*hold_time
    circ.speed = speed
    return circ

"""
Generate 2 circles
they cannot be the same
return a tuple of both circles
"""
def generate_double_circle(startcircles):
    num_1 = random.randint(0,7)
    num_2 = random.randint(0,7)
    while num_1 == num_2:
        num_2 = random.randint(0,7)
    circ1 = copy.copy(startcircles[num_2])
    circ2 = copy.copy(startcircles[num_2])
    circ1.color1 = [255,255,0]
    circ1.color2 = [255,255,147]
    circ2.color1 = [255,255,0]
    circ2.color2 = [255,255,147]
    speed = random.randint(10, 30)
    circ1.speed = speed
    circ2.speed = speed
    return (circ1, circ2)

"""
Generate 1 star
consists of its current position, 2 outer positions and 1 random position
"""
def generate_star(window, startcircles):
    circ_s = copy.copy(startcircles[random.randint(0,7)])
    circ_e = copy.copy(startcircles[random.randint(0,7)])
    # should first and second point be able to be same point?
    while circ_s == circ_e:
        circ_e = copy.copy(startcircles[random.randint(0,7)])

    rotation = math.radians(random.randint(0,359))
    radius = window.get_height()/2 - window.get_height()/20.0 - 40

    e_x = radius * math.cos(rotation) + window.get_width()/2
    e_y = radius * math.sin(rotation) + window.get_height()/2 

    m_x = window.get_width()/2  + random.randint(0,100)*((e_x-(window.get_width()/2 )) /100.0)
    m_y = window.get_height()/2 + random.randint(0,100)*((e_y-(window.get_height()/2)) /100.0)

    x = window.get_width()/2
    y = window.get_height()/2

    return star(x, y, circ_s.e_x, circ_s.e_y, 
                m_x, m_y, circ_e.e_x, circ_e.e_y, 
                window.get_width()/2, window.get_height()/2,
                (0, 0, 255), (0, 0, 147))

"""
Generate 2 stars
uses generate_star()
"""
def generate_double_star(window, startcircles):
    star1 = generate_star(window, startcircles)
    star2 = generate_star(window, startcircles)
    star1.color1 = (255, 255, 0)
    star1.color2 = (255, 255, 147)
    star2.color1 = (255, 255, 0)
    star2.color2 = (255, 255, 147)
    return (star1, star2)
