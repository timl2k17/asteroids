from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import pygame, random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        # Update the position of the asteroid based on its velocity
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        rangle = random.uniform(20, 50)
        left_vector = self.velocity.rotate(rangle)
        right_vector = self.velocity.rotate(-rangle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        left_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        left_asteroid.velocity = left_asteroid.velocity * 1.2
        left_asteroid.velocity += left_vector
        right_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        right_asteroid.velocity = right_asteroid.velocity * 1.2
        right_asteroid.velocity += right_vector