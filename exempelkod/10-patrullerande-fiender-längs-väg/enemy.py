import pygame
from enum import Enum

class Enemy:
    # Vägen som fienderna ska följa
    # Vi hårdkodar här utifrån att skärmen är 800x600
    PATH = ((780,100),(780,200),(20,200),(20,300),(780,300),(780,400),(20,400),(20,500),(400,500),(400,600))
    class State(Enum):
        ALIVE = 1
        DEAD = 0

    def __init__(self, bounds, position):
        self.position = pygame.Vector2(position)
        self.bounds = bounds
        self.size = 10

        # Vi skapar en lista med vektorer av fiendens väg
        self.path = [pygame.Vector2(x,y) for x,y in Enemy.PATH]
        self.state = Enemy.State.ALIVE

        # Hanteringen av fiendens rörelse kring vägen
        # Vi sätter fiendens hastighet till att röra sig mot nästa punkt på vägen
        self.speed = 3
        self.path_index = 0
        self.next_position = self.path[self.path_index]
        # Vi sätter fiendens hastighet till att röra sig mot nästa punkt på vägen
        self.velocity = self.next_position-self.position
        self.velocity.scale_to_length(self.speed)

    def get_rect(self):
        """
        Returnerar en rektangel som representerar fienden
        """
        return pygame.Rect(self.position.x-self.size, self.position.y-self.size, self.size*2, self.size*2)
    
    def update(self):
        """
        Uppdaterar fiendens position
        """
        if self.is_alive():
            # Om fienden är nära nästa punkt på vägen, sätt fiendens position till punkten
            # och uppdatera till nästa punkt på vägen
            if self.position.distance_to(self.next_position) < self.speed:
                self.position = self.next_position
                self.path_index += 1
                # Om vi nått slutet på vägen, döda fienden
                if self.path_index >= len(self.path):
                    self.die()
                else:
                    self.next_position = self.path[self.path_index]
                    self.velocity = self.next_position-self.position
                    self.velocity.scale_to_length(self.speed)
            else:
                # Annars rör fienden sig mot nästa punkt på vägen
                self.position += self.velocity

    def die(self):
        """
        Dödar fienden
        """
        self.state = Enemy.State.DEAD

    def is_alive(self):
        """
        Returnerar om fienden är vid liv
        """
        return self.state == Enemy.State.ALIVE

    def draw(self, screen):
        """
        Ritar fienden
        """
        if self.is_alive():
            pygame.draw.circle(screen, "red", self.position, self.size)