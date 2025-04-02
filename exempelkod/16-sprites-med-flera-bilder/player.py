import pygame

# Inför konstanter för riktningarna
LEFT = 0
DOWN = 1
UP = 2
RIGHT = 3

class Player(pygame.sprite.Sprite):
    def __init__(self, x=100, y=100):
        super().__init__()
        self.speed = 4
        image = pygame.image.load("boy.png")
        # Vi använder listor av listor för att göra
        # koden smidig
        self.images = []
        # Vi laddar in bilder för alla fyra riktningar
        for column_idx in range(0,4):
            # Lägg till en lista för bilderna i denna rimtning
            direction = []
            self.images.append(direction)
            # För varje riktning finns fyra bilder
            for row_idx in range(0,4):
                subimage = image.subsurface((column_idx*64,row_idx*64,64,64))
                direction.append(subimage)
        # Börja med att titta åt vänster
        self.direction = LEFT
        self.image = self.images[self.direction][0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def update(self, keys):
        dx = 0
        dy = 0

        # Genom att ha elif på alla knapparna kan vi inte längre
        # gå diagonalt. Det blir alltid bara en rörelse, antingen
        # dx eller dy
        if keys[pygame.K_LEFT]:
            dx = -1
            self.direction = LEFT
        elif keys[pygame.K_RIGHT]:
            dx = 1
            self.direction = RIGHT
        elif keys[pygame.K_UP]:
            dy = -1
            self.direction = DOWN
        elif keys[pygame.K_DOWN]:
            dy = 1
            self.direction = UP

        if dx != 0 or dy != 0:
            # Nu behövs alltså inte skalningen längre,
            # men den gör ingen större skada
            length = (dx ** 2 + dy ** 2) ** 0.5
            self.rect.x += dx / length * self.speed
            self.rect.y += dy / length * self.speed

            # Ändra bara bild när spelaren rör sig
            # för förhindra att bilden skall animeras när
            # spelaren står still
            now = pygame.time.get_ticks()
            # Använd modulo-operatorn för att byta bild till nästa
            # med jämna mellanrum (150 ms)
            index = (now//150) % len(self.images[self.direction])
            # Välj bild baserat på index
            self.image = self.images[self.direction][index] 
