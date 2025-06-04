import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            child_size = self.radius - ASTEROID_MIN_RADIUS
            child_1 = Asteroid(*self.position, child_size)
            child_1.velocity = self.velocity.rotate(angle) * 1.2
            child_2 = Asteroid(*self.position, child_size)
            child_2.velocity = self.velocity.rotate(-angle) * 1.2
