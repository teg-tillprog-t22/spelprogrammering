import pygame

class Enemy:
    PATH = ((780,100),(780,200),(20,200),(20,300),(780,300),(780,400),(20,400),(20,500),(780,500),(780,600))

    def __init__(self, position, bounds, speed=3, size=10):
        self.position = position
        self.bounds = bounds
        self.size = size
        self.step = 0
        self.path = [pygame.Vector2(x,y) for x,y in Enemy.PATH]
        self.speed = speed
        self.velocity = (self.path[self.step]-self.position).normalize() * self.speed
        self.is_alive = True

    def update(self):
        if self.is_alive:
            if self.position.distance_to(self.path[self.step]) < self.speed:
                self.position = self.path[self.step]
                self.step += 1
                if self.step >= len(self.path):
                    self.die()
                else:
                    self.velocity = (self.path[self.step]-self.position).normalize() * self.speed
            else:
                self.position += self.velocity

    def die(self):
        self.is_alive = False

    def draw(self, screen):
        if self.is_alive:
            pygame.draw.circle(screen, "red", self.position, self.size)