import math
"""
blue X to click 
x,y: current position
s_x, s_y: start point
e_x, e_y: end point
color1: main color
color2: secondary color

TODO
speed: 
"""
class tap:
    def __init__(self, x, y, color1, color2):
        self.x = x
        self.y = y
        self.color1 = color1
        self.color2 = color2
        self.radius = 18
        self.timer = 50
        self.scored = False

    def update(self):
        self.timer = self.timer-1
        if self.timer < 1:
            return False, 1
        return True, 0
    
    def intersection(self, x, y):
        length_x = abs(x - self.x)
        length_y = abs(y - self.y)

        length = math.sqrt(math.pow(length_x,2) + math.pow(length_y, 2)) 

        if length < self.radius:
            return True
        return False

"""
Used to control a large (small) amount of taps
"""
class taps():
    def __init__(self):
        self.taps = []

    def add(self, circle):
        self.taps.append(circle)

    def get_taps(self):
        return self.taps
    
    def remove_tap(self, tap):
        try:
            self.taps.remove(tap)
        except:
            print("tap is not in taps")

    def update(self):
        misses = 0
        for tap in self.taps:
            (keep_bool, miss) = tap.update()
            misses += miss
            if keep_bool == False:
                self.taps.remove(tap)
        return misses
    
    def check_for_points(self, x, y):
        score = 0
        for tap in self.taps:
            intersect_bool = tap.intersection(x, y)
            if intersect_bool == True:
                score += 1
                tap.scored = True
                self.taps.remove(tap)
        return score