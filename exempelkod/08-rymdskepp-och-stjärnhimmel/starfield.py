import pygame
from random import randint, random

class Star:
    def __init__(self, bounds, position=None, size=2, color="white"):
        """
        Skapa en stjärna, slumpmässigt placerad inom "bounds"
        """
        self.bounds = pygame.Rect(bounds)
        if position:
            self.position = pygame.Vector2(position)
        else:
            self.position = pygame.Vector2(randint(self.bounds.left, self.bounds.right), randint(self.bounds.top, self.bounds.bottom))
        self.size = size
        self.color = color

    def draw(self, screen):
        """
        Rita ut stjärnan på skärmen
        """
        pygame.draw.circle(screen, self.color, self.position, self.size)

    def update(self, velocity):
        """
        Uppdatera stjärnans position
        """
        # Kolla om stjärnan är utanför skärmen
        if not self.bounds.collidepoint(self.position) and (velocity.x!=0 or velocity.y!=0):
            # Placera stjärnan på motsatt sida av skärmen
            # Avgör om vi ska placera stjärnan på x- eller y-axeln
            # beroende på vilken hastighet vi "har mest av"
            if random()>abs(velocity.x)/(abs(velocity.x)+abs(velocity.y)):
                # Placera stjärnan i över- eller nederkant
                x = randint(0, self.bounds.width)
                y = self.bounds.top if velocity.y>0 else self.bounds.bottom
            else:
                # Placera stjärnan i vänster- eller högerkant
                x = self.bounds.left if velocity.x>0 else self.bounds.right
                y = randint(0, self.bounds.height)
            self.position = pygame.Vector2(x, y)
        # Flytta stjärnan
        self.position += velocity

class StarField:
    """
    En klass som representerar en stjärnhimmel
    """
    def __init__(self, bounds, number_of_stars=100):
        """
        Skapa en stjärnhimmel med en begränsningsyta och ett antal stjärnor
        """
        self.bounds = pygame.Rect(bounds)
        self.stars = [Star(self.bounds) for _ in range(number_of_stars)]

    def draw(self, screen):
        """
        Rita ut stjärnhimlen på skärmen
        """
        # Rita ut varje stjärna
        for star in self.stars:
            star.draw(screen)

    def update(self, velocity):
        """
        Uppdatera stjärnhimlen
        """
        # Uppdatera varje stjärna
        for star in self.stars:
            star.update(velocity)
