from circleshape import CircleShape;
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS;
import pygame, random;
from logger import log_event;
from random import choice;

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        self.x = x;
        self.y = y;
        self.radius = radius;
        self.color = random.choice(["salmon", "cyan", "yellow", "magenta", "bisque"]);
        super().__init__(self.x,self.y,self.radius);
        

    def draw(self,screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius);
    
    
    def update(self,dt):
        self.position += self.velocity*dt;

    def split(self):

        self.kill();

        if self.radius <= ASTEROID_MIN_RADIUS:
            return;
        else:
            log_event("asteroid_split");
            split_angle = random.uniform(20, 50);
            astrd1_velocity = self.velocity.rotate(split_angle);
            astrd2_velocity = self.velocity.rotate(-split_angle);

            astrd1_radius = self.radius - ASTEROID_MIN_RADIUS;
            astrd2_radius  = self.radius - ASTEROID_MIN_RADIUS;

            astrd1 = Asteroid(self.position.x, self.position.y, astrd1_radius);
            astrd1.velocity = astrd1_velocity * 1.2;

            astrd2 = Asteroid(self.position.x, self.position.y, astrd2_radius);
            astrd2.velocity = astrd2_velocity * 1.2;



