import pygame
import random

COIN_SIZE = 50
COIN_IMAGE = pygame.image.load("coin.png")
COIN_IMAGE = pygame.transform.scale(COIN_IMAGE, (COIN_SIZE, COIN_SIZE))

class Candy(pygame.sprite.Sprite):
    def __init__(self, area: pygame.Rect):
        super().__init__()
        self.area = area
        self.x = random.randint(area.left, area.right - COIN_SIZE)
        self.y = area.top - COIN_SIZE
        self.speed = random.randint(1,5)
        self.image = COIN_IMAGE
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def update(self):
        self.y += self.speed
        if self.y > self.area.bottom:
            # Om godiset hamnar utanför skärmen
            # så markerar vi det för borttagning
            # ur alla spritegrupper
            self.kill()

        self.rect.topleft = (self.x, self.y)


