from circleshape import CircleShape;
from constants import LINE_WIDTH;
import pygame;

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        self.x = x;
        self.y = y;
        self.radius = radius;
        super().__init__(self.x,self.y,self.radius);
        

    def draw(self,screen):
        pygame.draw.circle(screen, "black", self.position, self.radius);
    
    
    def update(self,dt):
        self.position += self.velocity*dt;

