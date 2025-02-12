import pygame
from enum import Enum

class Player:
    """Representerar spelaren."""
    # Den här spelaren gör för närvarande ingenting utan placeras bara i mitten av skärmen
    # Den innehåller i övrigt bara vår standardstruktur för klasser med spelobjekt
    # såsom init(), update(), draw() och get_rect()

    def __init__(self, bounds):
        """Skapa en spelare."""
        self.bounds = pygame.Rect(bounds)
        self.position = pygame.Vector2(self.bounds.center)
        self.size = 20
        self.color = "yellow"

    def update(self, keys):
        """Uppdatera spelarens position och tillstånd.
        Reagera på knapptryckningar."""
        pass

    def draw(self, screen):
        """Rita ut spelaren på skärmen."""
        pygame.draw.circle(screen, self.color, self.position, self.size)
        pass

    def get_rect(self):
        """Returnerar spelarens hit box"""
        return pygame.Rect(
            self.position - (self.size, self.size), (self.size * 2, self.size * 2)
        )

    def check_collisions(self, enemies):
        """Kontrollerar om spelaren kolliderar med andra objekt
        och sköter logiken för vad som händer vid kollisioner."""
        pass