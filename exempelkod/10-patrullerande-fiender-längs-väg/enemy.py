import pygame
from enum import Enum

class Enemy:
    PATH = ((780,100),(780,200),(20,200),(20,300),(780,300),(780,400),(20,400),(20,500),(400,500),(400,600))
    class State(Enum):
        ALIVE = 1
        DEAD = 0

    def __init__(self, position, bounds, speed=3, size=10):
        self.position = pygame.Vector2(position)
        self.bounds = bounds
        self.size = size
        self.step = 0
        self.path = [pygame.Vector2(x,y) for x,y in Enemy.PATH]
        self.speed = speed
        self.velocity = (self.path[self.step]-self.position).normalize() * self.speed
        self.state = Enemy.State.ALIVE

    def get_rect(self):
        return pygame.Rect(self.position.x-self.size, self.position.y-self.size, self.size*2, self.size*2)
    
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
        self.state = Enemy.State.DEAD

    def is_alive(self):
        return self.state == Enemy.State.ALIVE

    def draw(self, screen):
        if self.is_alive():
            pygame.draw.circle(screen, "red", self.position, self.size)