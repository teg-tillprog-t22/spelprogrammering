import pygame
from math import sin, cos, pi
from random import randint, choice
from enum import Enum

# KONSTANTER

WIDTH = 800
HEIGHT = 600
FPS = 60

# KLASSER

class Player:
    """
    Representerar spelaren
    """

    def __init__(self, x=100, y=100):
        """
        Initialisera spelarens attribut med startvärden 
        """
        self.x = x
        self.y = y
        self.size = 20      # Storlek i pixlar
        self.direction = 0  # Riktning i radianer
        self.speed = 3      # Hastighet i pixlar per fram
        self.points = 0

    def update(self, keys):
        """
        Uppdatera spelarens position och tillstånd
        Reagera på knapptryckningar
        """
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
        if self.x > WIDTH-self.size or self.x < self.size:
            # Utgångsvinkeln är pi - ingångsvinkeln vid kollision på sidorna
            # Rita på papper för att övertyga dig om att detta är sant
            self.direction = pi - self.direction

        # y-led
        if self.y > HEIGHT-self.size or self.y < self.size:
            # Utgångsvinkeln är -ingångsvinkeln vid kollision uppåt/nedåt
            # Rita på papper för att övertyga dig om att detta är sant
            self.direction = -self.direction

    def draw(self, screen):
        """
        Rita ut spelaren på skärmen.
        """
        now = pygame.time.get_ticks()
        # Rita spelarens kropp som en cirkel
        pygame.draw.circle(screen, "yellow", (self.x, self.y), self.size)
        # Och lägg till ett streck från origo till cirkelns
        # kant för att visa riktningen
        x1 = self.x + self.size*cos(self.direction)
        y1 = self.y + self.size*sin(self.direction)
        pygame.draw.line(screen, "black", (self.x, self.y), (x1,y1), 2)

    def get_rect(self):
        """Returnerar spelarens hit box"""
        return pygame.Rect(
            self.x-self.size, self.y-self.size, self.size*2, self.size*2)

    def check_collisions(self, candies):
        """
        Kontrollerar om spelaren kolliderar med andra objekt
        och sköter logiken för vad som händer vid kollisioner
        """
        for candy in candies:
            if candy.is_active() and self.get_rect().colliderect(candy.get_rect()):
                candy.die()
                self.points += 100

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
        

# FUNKTIONER
def create_random_candy():
    size = 10
    x = randint(size, WIDTH-size)
    y = randint(size, HEIGHT-size)
    color = choice(["red", "green", "blue"])
    lifetime = randint(3000, 10000)
    candy = Candy(x, y, color, size, lifetime)
    return candy

def main():
    """
    Spelets huvudfunktion.
    Motsvarar en spelomgång i vårt spel.
    """

    # Intialisera pygame och font-modulen
    pygame.init()
    pygame.font.init()

    # Skapa en skärm att rita på och en klocka som
    # håller reda på tiden och våra frames
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()

    # Välj en standardfont
    font = pygame.font.Font(None, 36)

    # Initialisera spelvärlden
    player = Player()
    candies = []
    
    running = True
    while running:
        # Flytta fram frame/tid
        dt = clock.tick(FPS)
        now = pygame.time.get_ticks()
    
        # Hantera händelser (events)
        for evt in pygame.event.get():
            if evt.type==pygame.QUIT:
                running = False

        # Uppdatera spelvärlden/logiken

        # - Rörelser
        keys = pygame.key.get_pressed()
        player.update(keys)
        for candy in candies:
            candy.update()

        # - Kollsioner
        player.check_collisions(candies)

        # - Städa upp döda objekt
        # (Vi kan använda en list comprehension istället för nedan)
        candies = [c for c in candies if c.is_alive()]

        # - Skapa nya objekt
        # Logiken hade kunnat vara på många sätt
        # men här skapar vi tre i taget så fort
        # ingen längre är aktiv
        # (Vi kan använda en vanlig loop istället för sum nedan)
        num_active = sum(c.is_active() for c in candies)
        if num_active==0:
           for i in range(3):
                candies.append(create_random_candy())

        # Rita ut spelvärlden
        screen.fill("black")
        for candy in candies:
            candy.draw(screen)
        player.draw(screen)

        # Rita ut poängen på skärmen
        text = f"Score: {player.points}"
        text_surface = font.render(text, True, "white")  
        screen.blit(text_surface, (10, 10))  # Top-left corner        
       
        # Flippa skärmen
        pygame.display.flip()

    pygame.quit()

# HUVUDPROGRAMMET
main()
