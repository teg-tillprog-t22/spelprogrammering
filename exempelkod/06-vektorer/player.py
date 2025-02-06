import pygame
from math import sin, cos, pi

class Player:
    '''
    Representerar spelaren
    '''

    def __init__(self, width, height):
        '''
        Initialisera spelarens attribut med startvärden 
        '''
        self.x = width//2
        self.y = height//2
        self.size = 20      # Storlek i pixlar
        self.direction = 0  # Riktning i radianer
        self.speed = 3      # Hastighet i pixlar per fram
        self.points = 0
        self.width = width
        self.height = height

    def update(self, keys):
        '''
        Uppdatera spelarens position och tillstånd
        Reagera på knapptryckningar
        '''
        # Piltangenterna används för att förändra spelarens
        # riktining med 1/100 varv
        if keys[pygame.K_LEFT]:
            self.direction -= 2*pi/100
        if keys[pygame.K_RIGHT]:
            self.direction += 2*pi/100

        # Beräkna nya x från förflyttningen
        # med hjälp av lite trigonometri 
        self.x += self.speed*cos(self.direction)
        self.y += self.speed*sin(self.direction)

        # Kontrollera om de nya koordinaterna går utanför kanten
        # på skärmen

        # x-led
        if self.x > self.width-self.size or self.x < self.size:
            # Utgångsvinkeln är pi - ingångsvinkeln vid kollision på sidorna
            # Rita på papper för att övertyga dig om att detta är sant
            self.direction = pi - self.direction

        # y-led
        if self.y > self.height-self.size or self.y < self.size:
            # Utgångsvinkeln är -ingångsvinkeln vid kollision uppåt/nedåt
            # Rita på papper för att övertyga dig om att detta är sant
            self.direction = -self.direction

    def draw(self, screen):
        '''
        Rita ut spelaren på skärmen.
        '''
        now = pygame.time.get_ticks()
        # Rita spelarens kropp som en cirkel
        pygame.draw.circle(screen, "yellow", (self.x, self.y), self.size)
        # Och lägg till ett streck från origo till cirkelns
        # kant för att visa riktningen
        x1 = self.x + self.size*cos(self.direction)
        y1 = self.y + self.size*sin(self.direction)
        pygame.draw.line(screen, "black", (self.x, self.y), (x1,y1), 2)

    def get_rect(self):
        '''Returnerar spelarens hit box'''
        return pygame.Rect(
            self.x-self.size, self.y-self.size, self.size*2, self.size*2)

    def check_collisions(self, candies):
        '''
        Kontrollerar om spelaren kolliderar med andra objekt
        och sköter logiken för vad som händer vid kollisioner
        '''
        for candy in candies:
            if candy.is_active() and self.get_rect().colliderect(candy.get_rect()):
                candy.die()
                self.points += 100

