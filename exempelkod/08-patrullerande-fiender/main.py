import pygame
from enemy import Enemy

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
    bounds = screen.get_rect()
    enemies = [Enemy(pygame.Vector2(x, 100), bounds) for x in range(40,WIDTH-40,40)]
    
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
        for enemy in enemies:
            enemy.update()

        # - Rörelser
        keys = pygame.key.get_pressed()

        # - Kollisioner

        # - Städa upp döda objekt
        enemies = [enemy for enemy in enemies if enemy.is_alive]

        # - Skapa nya objekt

        # Rita ut spelvärlden
        screen.fill("black")
        for enemy in enemies:
            enemy.draw(screen)

        # Flippa skärmen
        pygame.display.flip()

    pygame.quit()

# HUVUDPROGRAMMET
main()
