import pygame
import sys
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)

def main():
    pygame.init()
    FPS = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color= (0, 0, 0))
        for drawing in drawable:
            drawing.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if Asteroid.collision_check(asteroid, player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if Asteroid.collision_check(asteroid, shot):
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()

        dt = FPS.tick(60) / 1000

if __name__ == "__main__":
    main()
