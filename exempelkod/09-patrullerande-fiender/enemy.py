import pygame
from enum import Enum

class Enemy:
    class State(Enum):
        ALIVE = 1
        DEAD = 0

    def __init__(self, bounds, position, velocity):
        self.position = pygame.Vector2(position)
        self.velocity = pygame.Vector2(velocity)
        self.bounds = pygame.Rect(bounds)
        self.size = 10
        self.color = "red"
        self.state = Enemy.State.ALIVE

    def get_rect(self):
        """
        Returnera en hitbox med fiendens position och storlek
        """
        return pygame.Rect(self.position.x-self.size, self.position.y-self.size, self.size*2, self.size*2)
    
    def update(self):
        """
        Uppdatera fiendens position och rörelse
        """
        # Flytta bara spelaren om den är aktiv (dvs vid liv eftersom det bara finns två states)
        if self.is_alive():
            # Uppdatera positionen
            self.position += self.velocity
            # Kolla om spelaren är utanför skärmen
            if not self.bounds.contains(self.get_rect()):
                # Om spelaren är utanför skärmen, flytta tillbaka den och byt riktning
                self.velocity = -self.velocity
                self.position += self.velocity

    def die(self):
        """
        Döda fienden (anropas t ex av ett skott om det träffar)
        """
        self.state = Enemy.State.DEAD

    def is_alive(self):
        """
        Returnera True om fienden är vid liv, annars False
        """
        return self.state == Enemy.State.ALIVE

    def draw(self, screen):
        """
        Rita ut fienden på skärmen
        """
        if self.is_alive():
            pygame.draw.circle(screen, self.color, self.position, self.size)

