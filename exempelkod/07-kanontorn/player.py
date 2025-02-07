import pygame
from math import pi
class Player:
    '''
    Representerar spelaren
    '''

    def __init__(self, width, height):
        '''
        Initialisera spelarens attribut med startvärden 
        '''
        self.color = "yellow"
        self.size = 50
        self.cannon_size = 70
        self.position = pygame.Vector2(width//2, height-51)
        self.points = 0
        self.angle = 200
        self.speed = 180/50

    def update(self, keys):
        '''
        Uppdatera spelarens position och tillstånd
        Reagera på knapptryckningar
        '''
        self.angle += self.speed
        if self.angle>350 or self.angle<190:
            self.speed = -self.speed
            self.angle += self.speed   


    def draw(self, screen):
        '''
        Rita ut spelaren på skärmen.
        '''
        # Rita kanontornet
        pygame.draw.circle(screen, "blue", self.position, self.size, draw_top_left=True, draw_top_right=True)
        # Rita pipan som en polygon som vi roterar till rätt vinkel
        points = [
            self.position + pygame.Vector2(40,5).rotate(self.angle),
            self.position + pygame.Vector2(40,-5).rotate(self.angle),
            self.position + pygame.Vector2(70,-5).rotate(self.angle),
            self.position + pygame.Vector2(70,5).rotate(self.angle)
        ]
        pygame.draw.polygon(screen, "blue", points)
    
    
    def get_rect(self):
        '''Returnerar spelarens hit box'''
        return pygame.Rect(self.position-(self.size, self.size), (self.size*2, self.size*2)) 

    def check_collisions(self, candies):
        '''
        Kontrollerar om spelaren kolliderar med andra objekt
        och sköter logiken för vad som händer vid kollisioner
        '''

