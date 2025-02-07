import pygame
from player import Player

# KONSTANTER

WIDTH = 800
HEIGHT = 600
FPS = 60

# KLASSER


# FUNKTIONER

def main():
    '''
    Spelets huvudfunktion.
    Motsvarar en spelomgång i vårt spel.
    '''

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
    player = Player(WIDTH,HEIGHT)
    
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
        # Rita marken
        pygame.draw.rect(screen, "green", (0,HEIGHT-50,WIDTH,50))
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
