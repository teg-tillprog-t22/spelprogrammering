import pygame
from enum import Enum
from starfield import StarField

class Bullet:
    """
    Representerar ett skott
    """
    
    class State(Enum):
        ALIVE = 1
        DEAD = 0

    def __init__(self, bounds, position, velocity, size=2):
        self.bounds = pygame.Rect(bounds)
        self.position = pygame.Vector2(position)
        self.velocity = pygame.Vector2(velocity)
        self.state = Bullet.State.ALIVE
        self.size = size

    def update(self):
        """
        Uppdatera skottets position
        """
        # Flytta skottet
        self.position += self.velocity
        # Kolla om skottet är utanför skärmen
        if not self.bounds.collidepoint(self.position):
            self.die()  

    def die(self):
        """
        "Dödar" skottet
        """
        self.state = Bullet.State.DEAD

    def is_alive(self):
        """
        False om skottet ska tas bort, annars True
        """
        return self.state == Bullet.State.ALIVE

    def draw(self, screen):
        """
        Rita ut skottet på skärmen
        """
        pygame.draw.circle(screen, "green", self.position, self.size)


class Player:
    """
    Representerar spelaren
    """

    # Konstanter

    # Rymdskeppets form
    SHIP_SHAPE = (
        (-20, 5),
        (-15, -10),
        (-10, 5),
        (0, -25),
        (10, 5),
        (15, -10),
        (20, 5),
    )

    # Brännarnas form
    BURNER_SHAPES = (((-18, 6), (-15, 12), (-12, 6)), ((18, 6), (15, 12), (12, 6)))

    # Hastigheter och krafter
    BULLET_SPEED = 5
    ANGULAR_SPEED = 180 / 50
    BURNER_FORCE = 0.1

    def __init__(self, bounds):
        """
        Initialisera spelarens attribut med startvärden
        """
        # Position
        self.bounds = pygame.Rect(bounds)
        self.position = pygame.Vector2(self.bounds.centerx, self.bounds.centery)

        # Utseende
        self.color = "yellow"
        self.burner = False

        # Poäng
        self.points = 0
        
        # Rörelse
        self.angle = 0
        self.acceleration = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(0, 0)

        # Skott
        self.bullets = []
        self.fire_delay = 100
        self.last_shot = 0
        
        # Bakgrund
        self.starfield = StarField(self.bounds)

    def update(self, keys):
        """
        Uppdatera spelarens position och tillstånd
        Reagera på knapptryckningar
        """
        # Kontroll av spelarens rörelse
        if keys[pygame.K_LEFT]:
            self.angle -= Player.ANGULAR_SPEED
        if keys[pygame.K_RIGHT]:
            self.angle += Player.ANGULAR_SPEED
        if keys[pygame.K_UP]:
            # Beräkna accelerationen
            acceleration = Player.BURNER_FORCE * pygame.Vector2(0, -1).rotate(self.angle)
            self.velocity += acceleration
            self.burner = True
        if keys[pygame.K_SPACE]:
            self.shoot()

        # Skeppet står stilla i mitten av skärmen
        # Uppdatera bakgrunden med motsatt hastighet
        self.starfield.update(-self.velocity)

        # Uppdatera skotten 
        for bullet in self.bullets:
            bullet.update()

        # Ta bort "döda" skott
        self.bullets = [bullet for bullet in self.bullets if bullet.is_alive()]

    def shoot(self):
        """
        Skjut ett skott
        """
        now = pygame.time.get_ticks()
        # Kontrollera att det har gått tillräckligt lång tid sedan förra skottet
        if now - self.last_shot > self.fire_delay:
            self.last_shot = now
            # Beräkna skottets hastighet och position
            bullet_velocity = Player.BULLET_SPEED * pygame.Vector2(0, -1).rotate(self.angle)
            bullet_position = self.position + pygame.Vector2(0, -25).rotate(self.angle)
            # Skapa skottet och lägg till det i listan
            bullet = Bullet(self.bounds, bullet_position, bullet_velocity, 3)
            self.bullets.append(bullet)

    def draw(self, screen):
        """
        Rita ut spelaren på skärmen.
        """
        # Beräkna punkterna för rymdskeppet
        # genom att rotera och flytta varje punkt enligt skeppets position och vinkel
        points = [
            self.position + pygame.Vector2(x, y).rotate(self.angle)
            for x, y in Player.SHIP_SHAPE
        ]
        # Rita ut rymdskeppet
        pygame.draw.polygon(screen, self.color, points)

        # Rita ut eldstrålarna om brännaren är på
        if self.burner:
            for shape in Player.BURNER_SHAPES:
                # Beräkna punkterna för eldstrålen
                # genom att rotera och flytta varje punkt enligt skeppets position och vinkel
                points = [
                    self.position + pygame.Vector2(x, y).rotate(self.angle)
                    for x, y in shape
                ]
                # Rita ut eldstrålen
                pygame.draw.polygon(screen, "red", points)

        # Rita ut skotten
        for bullet in self.bullets:
            bullet.draw(screen)

        # Rita ut stjärnhimlen
        self.starfield.draw(screen)

    def get_rect(self):
        """Returnerar spelarens hit box"""
        return pygame.Rect(
            self.position - (self.size, self.size), (self.size * 2, self.size * 2)
        )

    def check_collisions(self, enemies):
        """
        Kontrollerar om spelaren kolliderar med andra objekt
        och sköter logiken för vad som händer vid kollisioner
        """
