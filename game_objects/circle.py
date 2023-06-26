import math

"""
Purple/Yellow Circles 
x,y: current position
s_x, s_y: start point
e_x, e_y: end point
color1: main color
color2: secondary color
speed: travel speed
"""
class circle:
    def __init__(self, x, y, s_x, s_y, e_x, e_y, color1, color2, speed):
        self.x = x
        self.y = y
        self.s_x = s_x
        self.s_y = s_y
        self.e_x = e_x
        self.e_y = e_y
        self.color1 = color1
        self.color2 = color2
        self.hold_length = 0
        self.scored = False
        self.speed = speed
        self.radius = 18

    def update(self):
        max_length_x = self.s_x - self.e_x
        max_length_y = self.s_y - self.e_y

        cur_length_x = self.s_x - self.x
        cur_length_y = self.s_y - self.y

        if(abs(cur_length_x) < abs(max_length_x+max_length_x/self.speed) and abs(cur_length_y) < abs(max_length_y+max_length_y/30)):
            self.x = self.x - max_length_x/self.speed
            self.y = self.y - max_length_y/self.speed
        else: 
            reduction_length = math.sqrt(math.pow(max_length_x/self.speed,2) + math.pow(max_length_y/self.speed, 2))
            self.hold_length = self.hold_length-reduction_length
            
        if abs(cur_length_x) > abs(max_length_x)+self.hold_length and abs(cur_length_y) > abs(max_length_y)+self.hold_length:
            return False, 1
        return True, 0
    
    def intersection(self, x, y):
        length_x = abs(x - self.x)
        length_y = abs(y - self.y)
        length_ex = abs(x - self.e_x)
        length_ey = abs(y - self.e_y)

        length = math.sqrt(math.pow(length_x,2) + math.pow(length_y, 2)) 
        length_e = math.sqrt(math.pow(length_ex,2) + math.pow(length_ey, 2))

        # only intersecting when in range of the circle and the end position
        if length < self.radius and length_e < self.radius:
            return True
        return False
    
    def hold_over(self):
        max_length_x = self.s_x - self.e_x
        max_length_y = self.s_y - self.e_y
        cur_length_x = self.s_x - self.x
        cur_length_y = self.s_y - self.y
        if abs(cur_length_x) > abs(max_length_x)+self.hold_length-50 and \
        abs(cur_length_y) > abs(max_length_y)+self.hold_length-50:
            return True
        return False

"""
Used to control a large (small) amount of circles
"""
class circles():
    def __init__(self):
        self.circles = []

    def add(self, circle):
        self.circles.append(circle)

    def get_circles(self):
        return self.circles
    
    def remove_circle(self, circle):
        try:
            self.circles.remove(circle)
        except:
            print("circle is not in circles")

    def update(self):
        misses = 0
        for circle in self.circles:
            (keep_bool, miss) = circle.update()
            misses += miss
            if keep_bool == False:
                self.circles.remove(circle)
        return misses
    
    def check_for_points(self, x, y):
        score = 0
        for circle in self.circles:
            intersect_bool = circle.intersection(x, y)
            if intersect_bool == True:
                if circle.scored == False:
                    score += 1
                    circle.scored = True
                    if circle.hold_length <= 0:
                        self.circles.remove(circle)
                        continue
                else:
                    over_bool = circle.hold_over()
                    if over_bool == True:
                        score += 1
                        self.circles.remove(circle)
        return score