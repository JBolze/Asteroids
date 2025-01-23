import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    #game initialization. clock is for frame rate limitation
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    #groups setup for class iteration
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")
        for item in updatable:
            item.update(dt)
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()