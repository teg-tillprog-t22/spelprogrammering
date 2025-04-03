import pygame
import random

# Definiera bilden som en
COIN_IMAGE = pygame.transform.smoothscale(pygame.image.load("coin.png"), (32,32))

class Candy(pygame.sprite.Sprite):
    def __init__(self, area):
        super().__init__()
        # Area representerar skärmens storlek
        self.area = area
        self.image = COIN_IMAGE
        self.rect = self.image.get_rect()
        self.speed = 3
        # Slumpa placeringen av myntet
        x = random.randint(area.left, area.right - self.rect.width)
        y = random.randint(area.top, area.bottom - self.rect.height)
        # Sätt positionen på rektangeln själv
        self.rect.topleft = (x, y)
        self.created_at = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        # Godiset försvinner genom att döda sig själv efter 5 sekunder
        if now - self.created_at > 2000:
            self.kill()

