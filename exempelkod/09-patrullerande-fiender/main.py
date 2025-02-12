import pygame
from enemy import Enemy
from player import Player
from random import randint

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
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Välj en standardfont
    font = pygame.font.Font(None, 36)

    # Initialisera spelvärlden
    bounds = screen.get_rect()
    player = Player(bounds)
    enemies = [
        Enemy(bounds, (20, 100), (1, 0)),       # en fiende som börjar åt vänster och rör sig åt höger
        Enemy(bounds, (780, 200), (-1, 0))      # en fiende som börjar åt höger och rör sig åt vänster
        ]

    running = True
    while running:
        # Flytta fram frame/tid
        dt = clock.tick(FPS)
        now = pygame.time.get_ticks()

        # Hantera händelser (events)
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                running = False

        # Uppdatera spelvärlden/logiken
        keys = pygame.key.get_pressed()
        player.update(keys)
        for enemy in enemies:
            enemy.update()

        # - Rörelser
        keys = pygame.key.get_pressed()

        # - Kollisioner
        player.check_collisions(enemies)

        # - Städa upp döda objekt
        enemies = [enemy for enemy in enemies if enemy.is_alive()]

        # - Skapa nya objekt

        # Rita ut spelvärlden
        screen.fill("black")
        for enemy in enemies:
            enemy.draw(screen)
        player.draw(screen)

        # Flippa skärmen
        pygame.display.flip()

    pygame.quit()


# HUVUDPROGRAMMET
main()
