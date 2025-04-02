import pygame
import random

# Definiera bilden som en
COIN_IMAGE = pygame.image.load("coin.png")

class Candy(pygame.sprite.Sprite):
    def __init__(self, area):
        super().__init__()
        # Area representerar skärmens storlek
        self.area = area
        self.image = COIN_IMAGE
        self.rect = self.image.get_rect()
        self.speed = 3
        # Slumpa placeringen i x-led
        x = random.randint(area.left, area.right - self.rect.width)
        # Börja precis ovanför skärmens topp
        y = area.top - self.rect.height
        # Sätt positionen på rektangeln själv
        self.rect.topleft = (x, y)

    def update(self):
        # Vi ändrar y-värdet direkt i self.rect
        self.rect.y += self.speed

        if self.rect.y > self.area.bottom:
            # Om godiset hamnar utanför skärmen
            # så markerar vi det för borttagning
            # ur alla spritegrupper
            self.kill()

