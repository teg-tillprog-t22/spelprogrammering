import pygame
import random

# Definiera bilden som en
IMAGE = pygame.image.load("explosion.png")

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Area representerar skärmens storlek
        self.images = []
        for r in range(0,3):
            for c in range(0,3):
                self.images.append(IMAGE.subsurface(c*32, r*32, 32, 32))
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        # Sätt positionen på rektangeln
        self.rect.topleft = (x, y)
        self.created_at = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        index = (now - self.created_at)//100
        if index>=9:
            self.kill()
        else:
            self.image = self.images[index]

