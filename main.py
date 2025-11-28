import pygame;
from logger import log_state;
from constants import SCREEN_HEIGHT, SCREEN_WIDTH;
from player import Player;

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

    Player.containers = (updatable, drawable);

    p = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)

    


    # MAIN GAME LOOP

    while(True): 
        log_state();

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return;

        screen.fill("black");
        for sprite in drawable:
            sprite.draw(screen);
        
        pygame.display.flip();
        dt = gclock.tick(60)/1000;
        updatable.update(dt);
        #print(dt);

if __name__ == "__main__":
    main()
