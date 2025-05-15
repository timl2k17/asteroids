import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (updateable, drawable, asteroids)
    Player.containers = (updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
    af = AsteroidField()

    while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updateable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision_check(asteroid):
                    asteroid.split()
                    shot.kill()
            if player.collision_check(asteroid):
                print("Game over!")
                sys.exit(0)


        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()