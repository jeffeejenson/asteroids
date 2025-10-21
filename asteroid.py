from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y,radius)

    def draw():
        pygame.draw.circle(screen ,"white", self.postion , self.radius , 2)
    
        