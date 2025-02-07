import pygame

class Player:
    '''
    Representerar spelaren
    '''

    def __init__(self, width, height):
        '''
        Initialisera spelarens attribut med startvärden 
        '''
        self.position = pygame.Vector2(width//2, height//2)
        self.size = 20
        self.points = 0

    def update(self, keys):
        '''
        Uppdatera spelarens position och tillstånd
        Reagera på knapptryckningar
        '''

    def draw(self, screen):
        '''
        Rita ut spelaren på skärmen.
        '''

    def get_rect(self):
        '''Returnerar spelarens hit box'''
        return pygame.Rect(self.position-(self.size, self.size), (self.size*2, self.size*2)) 

    def check_collisions(self, candies):
        '''
        Kontrollerar om spelaren kolliderar med andra objekt
        och sköter logiken för vad som händer vid kollisioner
        '''

