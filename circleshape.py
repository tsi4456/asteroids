import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision_check(self, other):
        return self.position.distance_to(other.position) < (self.radius + other.radius)

    def wrap(self, screen):
        x, y = self.position
        screen_x = screen.get_width()
        screen_y = screen.get_height()
        if x + self.radius < 0:
            self.position.x += screen_x + self.radius * 2
        elif x - self.radius > screen_x:
            self.position.x -= screen_x + self.radius * 2
        if y + self.radius < 0:
            self.position.y += screen_y + self.radius * 2
        elif y - self.radius > screen_y:
            self.position.y -= screen_y + self.radius * 2
