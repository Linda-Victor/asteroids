import pygame
from constants import *
from player import *

def main():
    pygame.init()
    FPS = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color= (0, 0, 0))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()

        dt = FPS.tick(60) / 1000

if __name__ == "__main__":
    main()
