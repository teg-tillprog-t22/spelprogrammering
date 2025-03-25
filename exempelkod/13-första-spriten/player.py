import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x=100, y=100):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = 8
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect(topleft = (x,y))

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
            self.x += dx / length
            self.y += dy / length
            self.rect.topleft = (self.x, self.y)
            
    
