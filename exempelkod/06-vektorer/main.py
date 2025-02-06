import pygame
from random import randint, choice
from candy import Candy
from player import Player

# KONSTANTER

WIDTH = 800
HEIGHT = 600
FPS = 60

# KLASSER


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
        alive_candies = []
        for candy in candies:
            if candy.is_alive():
                alive_candies.append(candy)
        candies = alive_candies

        # - Skapa nya objekt
        # Logiken hade kunnat vara på många sätt
        # men här skapar vi tre i taget så fort
        # ingen längre är aktiv
        num_active = 0
        for candy in candies:
            if candy.is_active():
                num_active = num_active + 1
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
