import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x=100, y=100):
        super().__init__()
        self.speed = 8
        image = pygame.image.load("boy.png")
        self.image = image.subsurface((0,0,64,64))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def update(self, keys):
        dx = 0
        dy = 0

        if keys[pygame.K_LEFT]:
            dx = -1
        elif keys[pygame.K_RIGHT]:
            dx = 1
        
        if keys[pygame.K_UP]:
            dy = -1
        elif keys[pygame.K_DOWN]:
            dy = 1

        if dx != 0 or dy != 0:
            length = (dx ** 2 + dy ** 2) ** 0.5
            self.rect.x += dx / length * self.speed
            self.rect.y += dy / length * self.speed
