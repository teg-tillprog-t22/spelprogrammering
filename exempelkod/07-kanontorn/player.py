import pygame
from math import pi

class Bullet:
    ALIVE = 1
    DEAD = 0

    def __init__(self, position, angle):
        self.angle = angle
        self.speed = 5
        self.size = 4
        self.velocity = pygame.Vector2.from_polar((self.speed, self.angle))
        self.position = position + self.velocity.normalize()*70
        self.state = Bullet.ALIVE

    def update(self):
        self.position += self.velocity
        if self.position.x<0 or self.position.x>800 or self.position.y<0 or self.position.y>600:
            self.die()

    def die(self):
        self.state = Bullet.DEAD

    def is_alive(self):
        return self.state==Bullet.ALIVE

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.size)


class Player:
    '''
    Representerar spelaren
    '''

    def __init__(self, width, height):
        '''
        Initialisera spelarens attribut med startvärden 
        '''
        self.color = "yellow"
        self.size = 50
        self.cannon_size = 70
        self.position = pygame.Vector2(width//2, height-51)
        self.points = 0
        self.angle = 200
        self.speed = 180/50
        self.bullets = []
        self.fire_delay = 100
        self.last_shot = 0

    def update(self, keys):
        '''
        Uppdatera spelarens position och tillstånd
        Reagera på knapptryckningar
        '''        
        self.angle += self.speed
        if self.angle>350 or self.angle<190:
            self.speed = -self.speed
            self.angle += self.speed   
        
        for bullet in self.bullets:
            bullet.update()

        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.fire_delay:
            self.last_shot = now
            self.bullets.append(Bullet(self.position, self.angle))

    def draw(self, screen):
        '''
        Rita ut spelaren på skärmen.
        '''
        # Rita kanontornet
        pygame.draw.circle(screen, "blue", self.position, self.size, draw_top_left=True, draw_top_right=True)
        # Rita pipan som en polygon som vi roterar till rätt vinkel
        points = [
            self.position + pygame.Vector2(40,5).rotate(self.angle),
            self.position + pygame.Vector2(40,-5).rotate(self.angle),
            self.position + pygame.Vector2(70,-5).rotate(self.angle),
            self.position + pygame.Vector2(70,5).rotate(self.angle)
        ]
        pygame.draw.polygon(screen, "blue", points)

        self.bullets = [bullet for bullet in self.bullets if bullet.is_alive()]
        for bullet in self.bullets:
            bullet.draw(screen)
    
    
    def get_rect(self):
        '''Returnerar spelarens hit box'''
        return pygame.Rect(self.position-(self.size, self.size), (self.size*2, self.size*2)) 

    def check_collisions(self, candies):
        '''
        Kontrollerar om spelaren kolliderar med andra objekt
        och sköter logiken för vad som händer vid kollisioner
        '''

