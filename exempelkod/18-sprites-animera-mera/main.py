import random
import pygame
from player import Player
from candy import Candy
from explosion import Explosion

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

    # Gör en hjälpvariabel för att hålla reda på
    # spelplanens storlek (som vi gör till hela skärmen)
    area = screen.get_rect() 

    # Vi stoppar in spelaren i en spritegrupp
    # för att dra nytta av funktionalitet som finns
    # inbyggd i pygame
    players = pygame.sprite.Group()
    players.add(player) 

    # Skapa en tom spritegrupp för godisar
    candies = pygame.sprite.Group()

    # Och en för effekter som inte ska påverka spelet
    effects = pygame.sprite.Group()

    # Skapa en poängräknare
    score = 0

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
        candies.update()
        effects.update()

        # Skapa nya godisar slumpmässigt
        # ungefär varannan sekund
        if random.randint(1, FPS*2) == 1:
            candy = Candy(area)
            candies.add(candy)

        # Kontrollera kollisioner
        sprites = pygame.sprite.spritecollide(player, candies, True)
        for sprite in sprites:
            score += 100
            print(f"Totalpoäng: {score}")
            effects.add(Explosion(sprite.rect.x, sprite.rect.y))

        # OBS! Vi behöver inte städa upp sprites
        # Det gör pygame.sprite.Group automatiskt

        # Rita ut spelvärlden
        screen.fill("white")
        candies.draw(screen)
        players.draw(screen)
        effects.draw(screen)

        # Flippa skärmen
        pygame.display.flip()

    pygame.quit()


# HUVUDPROGRAMMET

if __name__ == "__main__":
    main()
