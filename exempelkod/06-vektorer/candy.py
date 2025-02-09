import pygame
from enum import Enum

class Candy:
    """
    Representerar en ätbar belöning i spelet
    """
    class State(Enum):
        """
        Anger tillståndet för en godis (aktiv, döende eller död)
        """
        
        ACTIVE = 1
        """Godisen är aktiv i spelet och går att äta"""
        
        DYING = 2
        """Godisen håller på att dö (animeras)"""
        
        DEAD = 3
        """Godisen är död och väntar på att bli bortstädad"""

    def __init__(self, x, y, color, size, lifetime):
        """
        Sätt startvärden för godisets attribut
        """
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.death_time = pygame.time.get_ticks() + lifetime
        self.state = Candy.State.ACTIVE

    def update(self):
        """
        Uppdaterar godisets position och tillstånd
        Den ligger mest still som godisar brukar
        """
        now = pygame.time.get_ticks()

        # Godiset agerar olika beroende på tillstånd
        match self.state:
            case Candy.State.ACTIVE:
                if now > self.death_time:
                    self.state = Candy.State.DEAD                    
            
            case Candy.State.DYING:
                # Om det har gått 2 sekunder så dö fullständigt
                if now > self.death_time + 2000:
                    self.state = Candy.State.DEAD

            case Candy.State.DEAD:
                # Väntar på bortstädning
                pass

    def get_rect(self):
        """
        Returnerar godisets hit box
        """
        return pygame.Rect(self.x-self.size, self.y-self.size, self.size*2, self.size*2)

    def die(self):
        """
        Påbörjar godisets dödsprocess (animering vid uppäten)
        """
        # Ändra state till DYING
        self.state = Candy.State.DYING
        now = pygame.time.get_ticks()
        # Återanvänd death_time för den faktiska dödstiden
        self.death_time = now

    def is_active(self):
        """
        Metod som anger att godiset är aktivt och kan ätas
        """
        return self.state==Candy.State.ACTIVE
    
    def is_alive(self):
        """
        Metod som anger att godiset är levande och inte ska städas bort
        """
        return self.state!=Candy.State.DEAD

    def draw(self, screen):
        """
        Rita godiset på skärmen.
        """
        now = pygame.time.get_ticks()

        # Beroende på state så ritas godiset ut på olika sätt
        match self.state:
            case Candy.State.ACTIVE:
                # Fancy blinkning sista sekunden
                time_until_death = self.death_time - now
                if time_until_death < 1000:
                    # Avrunda till 100ms och kontrollera
                    # om sista siffran är jämn eller udda
                    if time_until_death//100%2:
                        # Om jämn, rita inte ut figuren
                        # vilket blir resultatet av att
                        # hoppa ur funktionen 
                        return
                    
                # Rita ut godiset som en cirkel
                pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
            
            case Candy.State.DYING:
                time_since_death = now - self.death_time
                # Öka storleken med en pixel per 25 ms
                radius = self.size + time_since_death//25 
                # Rita ut godiset som en oifylld cirkel
                pygame.draw.circle(screen, self.color, (self.x, self.y), radius, 2)

            case Candy.State.DEAD:
                # Döda godisar ritas inte ut
                pass
        
