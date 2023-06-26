import math
""""
Stars with line

Purple/Yellow Circles 
x,y: current position --> begins at center
s_x, s_y: first goal (outer end position)
m_x, m_y: second goal on the map
e_x, e_y: last goal (outer end position)
color1: main color

TODO
speed: 
better implementation
"""
class star:
    def __init__(self, x, y, s_x, s_y, m_x, m_y, e_x, e_y, start_x, start_y, color1, color2):
        self.start_x = start_x
        self.start_y = start_y
        self.x = x
        self.y = y
        self.s_x = s_x
        self.s_y = s_y
        self.m_x = m_x
        self.m_y = m_y
        self.e_x = e_x
        self.e_y = e_y
        self.color1 = color1
        self.color2 = color2
        self.timer = 50
        self.radius = 30
        self.cp1 = False
        self.cp2 = False
        self.cp3 = False
        self.scored1 = False
        self.scored2 = False
        self.scored3 = False
        self.speed = 10
        self.lane_width = 5
    
    def update(self):
        misses = 0
        self.timer = self.timer-1

        def move(self, pos1, pos2):
            max_length_x = pos1[0] - pos2[0]
            max_length_y = pos1[1] - pos2[1]

            cur_length_x = pos1[0] - self.x
            cur_length_y = pos1[1] - self.y

            if(abs(cur_length_x) < abs(max_length_x) and abs(cur_length_y) < abs(max_length_y)):
                if max_length_x >= 0:
                    dir_x = 1
                else:
                    dir_x = -1

                if max_length_y >= 0:
                    dir_y = 1
                else:
                    dir_y = -1

                progress = self.speed
                edge_rel2 = max_length_x / max_length_y
                edge_rel = max_length_y / max_length_x

                # look star_math.png
                # still neeeds fix
                progress_x = math.sqrt(math.pow(progress,2)/math.pow(edge_rel,2) + math.pow(progress,2))
                progress_y = math.sqrt(math.pow(progress,2)/math.pow(edge_rel2,2) + math.pow(progress,2))
                # progress_y = math.sqrt(abs(math.pow(progress,2)- math.pow(progress_x,2)))

                self.x = self.x - dir_x*progress_x
                self.y = self.y - dir_y*progress_y
                return False
            else: 
                return True

        if(self.cp1 == False):
            self.cp1 = move(self, (self.start_x, self.start_y), (self.s_x,self.s_y))
            if self.scored1 == False and self.cp1 == True:
                self.scored1 = True
                misses = misses + 1
        elif(self.cp2 == False):
            self.cp2 = move(self, (self.s_x,self.s_y), (self.m_x,self.m_y))
            if self.scored2 == False and self.cp2 == True:
                self.scored2 = True
                misses = misses + 1
        elif(self.cp3 == False):
            self.cp3 = move(self, (self.m_x,self.m_y), (self.e_x,self.e_y))
            if(self.cp3 == True):
                if(self.scored3 == False):
                    self.scored3 = True
                    misses = misses + 1
                return False, misses
        return True, misses
    
    def intersection(self, x, y):
        length_x = abs(x - self.x)
        length_y = abs(y - self.y)
        length = math.sqrt(math.pow(length_x,2) + math.pow(length_y, 2))

        if self.scored1 == False:
            star_x = self.s_x
            star_y = self.s_y
            state = 0
        elif self.scored2 == False:
            star_x = self.m_x
            star_y = self.m_y
            state = 1
        elif self.scored3 == False:
            star_x = self.e_x
            star_y = self.e_y
            state = 2
        else: return False

        length_x = abs(x - star_x)
        length_y = abs(y - star_y)
        length2 = math.sqrt(math.pow(length_x,2) + math.pow(length_y, 2))

        if length < self.radius and length2 < self.radius:
            if state == 0: self.scored1 = True
            if state == 1: self.scored2 = True
            if state == 2: self.scored3 = True
            return True
        return False

"""
Used to control a large (small) amount of stars
"""
class stars():
    def __init__(self):
        self.stars = []

    def add(self, star):
        self.stars.append(star)

    def get_stars(self):
        return self.stars
    
    def remove_star(self, star):
        try:
            self.stars.remove(star)
        except:
            print("star is not in stars")

    def update(self):
        misses = 0
        for star in self.stars:
            (keep_bool, miss) = star.update()
            misses += miss
            if keep_bool == False:
                self.stars.remove(star)
        return misses
    
    def check_for_points(self, x, y):
        score = 0
        for star in self.stars:
            intersect_bool = star.intersection(x, y)
            if intersect_bool == True:
                score += 1
                star.scored = True
                if star.cp3 == True:
                    self.stars.remove(star)
        return score