import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x=100, y=100):
        super().__init__()
        self.speed = 8
        image = pygame.image.load("boy.png")
        self.image_left = image.subsurface((0,0,64,64))
        self.image_up = image.subsurface((64,0,64,64))
        self.image_down = image.subsurface((128,0,64,64))
        self.image_right = image.subsurface((196,0,64,64))
        # Börja med att titta åt vänster
        self.image = self.image_left
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
            self.image = self.image_left
        elif keys[pygame.K_RIGHT]:
            dx = 1
            self.image = self.image_right
        elif keys[pygame.K_UP]:
            dy = -1
            self.image = self.image_up
        elif keys[pygame.K_DOWN]:
            dy = 1
            self.image = self.image_down

        if dx != 0 or dy != 0:
            # Nu behövs alltså inte skalningen längre,
            # men den gör ingen större skada
            length = (dx ** 2 + dy ** 2) ** 0.5
            self.rect.x += dx / length * self.speed
            self.rect.y += dy / length * self.speed
