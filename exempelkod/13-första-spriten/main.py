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

    # Vi stoppar in spelaren i en spritegrupp
    # för att dra nytta av funktionalitet som finns
    # inbyggd i pygame
    players = pygame.sprite.Group()
    players.add(player) 

    # Vi gör samma sak med godisarna,
    # även om vi inte har några än
    candies = pygame.sprite.Group()

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
        players.update(keys)
        # Vi har inga godisar än, men OM vi hade haft det
        # skulle vi uppdatera dem här
        candies.update()

        # Rita ut spelvärlden
        screen.fill("black")
        # Fortfarande inga godisar, men här skulle vi ha ritat ut dem
        candies.draw(screen)
        players.draw(screen)

        # Flippa skärmen
        pygame.display.flip()

    pygame.quit()


# HUVUDPROGRAMMET

if __name__ == "__main__":
    main()
