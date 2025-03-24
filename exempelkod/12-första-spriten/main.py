import pygame
from player import Player

# KONSTANTER
WIDTH = 800
HEIGHT = 600
FPS = 60


# Huvudfunktionen som kör vårt spel
def main():
    # Initialisera pygame
    pygame.init()

    # Skapa en skärm att rita på och en klocka som
    # håller reda på tiden och våra frames
    screen = pygame.display.set_mode(
        (WIDTH, HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.SCALED, vsync=1
    )
    clock = pygame.time.Clock()

    # Initialisera spelvärlden
    player = Player(WIDTH // 2, HEIGHT // 2)
    candies = []

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
        for candy in candies:
            candy.update()

        # Rita ut spelvärlden
        screen.fill("black")
        for candy in candies:
            candy.draw(screen)
        player.draw(screen)

        # Flippa skärmen
        pygame.display.flip()

    pygame.quit()


# HUVUDPROGRAMMET

if __name__ == "__main__":
    main()
