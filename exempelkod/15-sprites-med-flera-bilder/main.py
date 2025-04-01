import pygame
from player import Player

# KONSTANTER
WIDTH = 800
HEIGHT = 600
FPS = 60


# Huvudfunktionen som kör vårt spel
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.SCALED, vsync=1)
    clock = pygame.time.Clock()

    """ HÄR ÄR DET NYTT"""
    player = Player(WIDTH // 2, HEIGHT // 2) # vi skapar ett spelarobjekt som vanligt
    players = pygame.sprite.Group() # här skapar vi en grupp med sprites som är spelare
    # vi skapar den gruppen som ett objekt i en klass som heter Group som finns i modulen sprite
    # gruppen gör att vi kan uppdatera, rita ut och kolla kollisioner på ett enkelt sätt

    players.add(player) # här lägger vi till vår spelare i gruppen, just i det här spelet har vi bara en


    running = True
    while running:
        dt = clock.tick(FPS)
        now = pygame.time.get_ticks()

        # Hantera händelser (events)
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                running = False

        # Uppdatera spelvärlden/logiken
        keys = pygame.key.get_pressed()

        """HÄR ÄR DET NYTT"""
        players.update(keys) # istället för att uppdatera en spelare så uppdaterar vi hela gruppen
        # det blir smidigt sen med tex godisar om det finns många

        # Rita ut spelvärlden
        screen.fill("black")

        """HÄR ÄR DET NYTT"""
        players.draw(screen) # här ritar vi ut alla spelare i gruppen
        # vi använder här den inbyggda metoden draw() som finns i Group-klassen, därför behövde vi inte vår egen draw()

        # Flippa skärmen
        pygame.display.flip()

    pygame.quit()


# HUVUDPROGRAMMET
main()
