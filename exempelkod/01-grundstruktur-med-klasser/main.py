import pygame
import math
import random

# KONSTANTER

WIDTH = 800
HEIGHT = 600
FPS = 60

# KLASSER

class Player:
    def __init__(self, x=100, y=100):
        self.x = x
        self.y = y
        self.size = 20 # Storlek i pixlar
        self.direction = 0 # Riktning i radianer
        self.speed = 3 # Hastighet i pixlar per 1/FPS s

    def update(self, keys):
        # Piltangenterna används för att förändra spelarens
        # riktining med 1/100 varv
        if keys[pygame.K_LEFT]:
            self.direction -= 2*math.pi/100
        if keys[pygame.K_RIGHT]:
            self.direction += 2*math.pi/100

        # Beräkna nya x från förflyttningen
        # med hjälp av lite trigonometri 
        self.x += self.speed*math.cos(self.direction)
        self.y += self.speed*math.sin(self.direction)

    def draw(self, screen):
        now = pygame.time.get_ticks()
        # Rita spelarens kropp som en cirkel
        pygame.draw.circle(screen, "yellow", (self.x, self.y), self.size)
        # Och lägg till ett streck från origon till cirkelns
        # kant för att visa riktningen
        x1 = self.x + self.size*math.cos(self.direction)
        y1 = self.y + self.size*math.sin(self.direction)
        pygame.draw.line(screen, "black", (self.x, self.y), (x1,y1), 2)

class Candy:
    def __init__(self):
        self.x = WIDTH//2
        self.y = HEIGHT//2
        self.color = "red"
        self.size = 10
        self.move_next_at = 0

    def update(self):
        now = pygame.time.get_ticks()
        if now > self.move_next_at:
            # Hårdkodat beteende för godisarna
            # 3-10 sekunders väntan och färgerna röd/grön/blå
            self.move_next_at = now + random.randint(3000,10000)
            self.color = random.choice(["red", "green", "blue"])
            self.x = random.randint(self.size, WIDTH-self.size)
            self.y = random.randint(self.size, HEIGHT-self.size)

    def draw(self, screen):
        now = pygame.time.get_ticks()
        # Fancy blinkning sista sekunden
        if self.move_next_at - now < 1000:
            # Avrunda till 100ms och kontrollera
            # om sista siffran är jämn eller udda
            if (self.move_next_at-now)//100%2:
                # Om jämn, rita inte ut figuren
                return 
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

# FUNKTIONER

# Huvudfunktionen som kör vårt spel
def main():
    # Initialisera pygame
    pygame.init()

    # Skapa en skärm att rita på och en klocka som
    # håller reda på tiden och våra frames
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()

    # Initialisera spelvärlden
    player = Player()
    candies = [Candy(), Candy(), Candy()]
    
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
        keys = pygame.key.get_pressed()
        player.update(keys)
        for candy in candies:
            candy.update()

        # Rita ut spelvärlden
        screen.fill("black")
        player.draw(screen)
        for candy in candies:
            candy.draw(screen)
       
        # Flippa skärmen
        pygame.display.flip()

    pygame.quit()

# HUVUDPROGRAMMET

main()
