import pygame

LEFT = 0
UP = 1
DOWN = 2
RIGHT = 3
class Player(pygame.sprite.Sprite):
    def __init__(self, x=100, y=100):
        super().__init__()
        self.speed = 8
        image = pygame.image.load("boy.png")
        self.images = []
        for c in range(0,4):
            direction = []
            self.images.append(direction)
            for r in range(0,4):
                direction.append(image.subsurface((c*64,r*64,64,64)))
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
            self.direction = UP
        elif keys[pygame.K_DOWN]:
            dy = 1
            self.direction = DOWN

        if dx != 0 or dy != 0:
            # Nu behövs alltså inte skalningen längre,
            # men den gör ingen större skada
            length = (dx ** 2 + dy ** 2) ** 0.5
            self.rect.x += dx / length * self.speed
            self.rect.y += dy / length * self.speed

            now = pygame.time.get_ticks()
            index = (now//150)%4
            self.image = self.images[self.direction][index]

        
        