import pygame, sys;
from logger import log_state, log_event;
from constants import SCREEN_HEIGHT, SCREEN_WIDTH;
from player import Player;
from asteroidfield import AsteroidField;
from asteroid import Asteroid;
from shot import Shot;

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}");
    print(f"Screen width: { SCREEN_WIDTH }");
    print(f"Screen height: {SCREEN_HEIGHT }");

    pygame.init();
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT));
    
    gclock = pygame.time.Clock();
    dt = 0;

    updatable = pygame.sprite.Group();
    drawable = pygame.sprite.Group();
    asteroids = pygame.sprite.Group();
    shots = pygame.sprite.Group();

    Player.containers = (updatable, drawable);
    Asteroid.containers = (asteroids, updatable, drawable);
    AsteroidField.containers = {updatable};
    Shot.containers = { shots, updatable, drawable };

    p = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2);
    astro_field = AsteroidField();
    
    print("All initial setup is complete");
    # MAIN GAME LOOP

    while(True): 
        log_state();

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return;

        screen.fill("white");
        
        for sprite in drawable:
            sprite.draw(screen);
        
        pygame.display.flip();
        dt = gclock.tick(60)/1000;
        
        updatable.update(dt);

        #print(f"Updated player position is {p.position}");
        
        for asteroid in asteroids:
            if p.collides_with(asteroid):
                log_event("player_hit");
                print("Game over!");
                sys.exit();
                

if __name__ == "__main__":
    main()
