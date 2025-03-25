import pygame

Vector = pygame.Vector2

class Player:
    def __init__(self, x=100, y=100):
        self.position = Vector(x,y)
        self.speed = 8
        self.image = pygame.image.load("player.png")
        # self.size = (64, 64)
        self.size = self.image.get_size()

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
            velocity = Vector(dx,dy) * self.speed
            self.position += velocity
                
    def get_rect(self):
        return pygame.Rect(self.position, self.size)

    def draw(self, screen):
        # Rita spelarens kropp
        # pygame.draw.rect(screen, "yellow", (self.position, self.size))
        screen.blit(self.image, self.position)

    
