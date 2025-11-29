import pygame;
from logger import log_state;
from constants import SCREEN_HEIGHT, SCREEN_WIDTH;
from player import Player;
from asteroidfield import AsteroidField;
from asteroid import Asteroid;

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

    Player.containers = (updatable, drawable);
    Asteroid.containers = (asteroids, updatable, drawable);
    AsteroidField.containers = {updatable};

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

if __name__ == "__main__":
    main()
