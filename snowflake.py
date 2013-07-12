import random
import pygame.gfxdraw
from pygame.locals import * #@UnusedWildImport

class Snowflake:
    def __init__(self, uid, width, height, radius, color):
        self.uid = uid
        self.width = width
        self.height = height
        self.radius = radius
        self.color = color
        self.gravity = random.uniform(5,15)
        self.pos = [random.randint(0, self.width), 0]
        self.enabled = True
        self.wind = 0        
        
    def update(self, gametime, snowflake_line):
        if self.enabled:
            speed = 1 / float(gametime)
            if not self.collision_check(snowflake_line):
                self.pos[1] += self.gravity * speed
            else:
                self.enabled = False
            if self.wind != 0:
                w = (self.gravity * speed)/8
                if self.wind < 0: w = -w                
                self.pos[0] += w
                self.wind -= w
            
    def collision_check(self, snowflake_line):        
        # check if it's hit the resting snow
        x = int(self.pos[0])
        y = self.pos[1]
        r = self.radius
        points = snowflake_line[x-r:x+r]        
        for p in points:
            if y + r >= p:
                for i in range(x-r, x+r):
                    if i >= 0 and i < self.width:
                        snowflake_line[i] = y
                return True
                    
        # check if it's on the bottom of the screen
        if self.pos[1] >= self.height: return True                 
        else: return False
    
    def draw(self, surface):
        pygame.gfxdraw.filled_circle(surface, int(self.pos[0]), int(self.pos[1]), self.radius, self.color)        
        pygame.gfxdraw.aacircle(surface, int(self.pos[0]), int(self.pos[1]), self.radius, self.color)