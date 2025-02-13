import pygame
from player import Player

# KONSTANTER

WIDTH = 800
HEIGHT = 600
FPS = 60

# KLASSER


# FUNKTIONER

def main():
    """
    Spelets huvudfunktion.
    Motsvarar en spelomgång i vårt spel.
    """

    # Intialisera pygame
    pygame.init()

    # Skapa en skärm att rita på och en klocka som
    # håller reda på tiden och våra frames
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()

    # Initialisera spelvärlden
    bounds = screen.get_rect()
    # Anpassa spelarens rörelseområde till skärmen minus marknivån
    bounds.bottom -= 50
    player = Player(bounds)
    
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

        # - Kollsioner
        player.check_collisions([])

        # - Städa upp döda objekt

        # - Skapa nya objekt

        # Rita ut spelvärlden
        screen.fill("black")
        
        # - Rita marken
        pygame.draw.rect(screen, "green", (0,HEIGHT-50,WIDTH,50))
        
        # - Rita spelaren
        player.draw(screen)

        # Flippa skärmen
        pygame.display.flip()

    pygame.quit()

# HUVUDPROGRAMMET
main()
