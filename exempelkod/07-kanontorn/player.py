import pygame


class Bullet:
    ALIVE = 1
    DEAD = 0

    def __init__(self, bounds, position, velocity):
        self.size = 4
        self.bounds = bounds
        self.position = position
        self.velocity = velocity
        self.state = Bullet.ALIVE

    def update(self):
        """Uppdatera skottets position."""
        self.position += self.velocity
        if not self.bounds.collidepoint(self.position):
            self.die()

    def die(self):
        """Döda skottet."""
        self.state = Bullet.DEAD

    def is_alive(self):
        """False om skottet ska tas bort, annars True."""
        return self.state == Bullet.ALIVE

    def draw(self, screen):
        """Rita ut skottet på skärmen."""
        pygame.draw.circle(screen, "white", self.position, self.size)


class Player:
    """Representerar spelaren."""

    def __init__(self, bounds):
        """Skapa en spelare."""
        # Initialisera spelarens attribut med startvärden
        # Utseende
        self.color = "yellow"
        self.size = 50
        self.cannon_size = 70
        # Position
        self.bounds = bounds
        self.position = pygame.Vector2(bounds.centerx, bounds.bottom - 1)
        # Poäng
        self.points = 0
        # Rörelse
        self.angle = 200
        self.speed = 180 / 50
        self.bullet_speed = 5
        # Skott
        self.bullets = []
        self.fire_delay = 100
        self.last_shot = 0

    def update(self, keys):
        """Uppdatera spelarens position och tillstånd.
        Reagera på knapptryckningar."""
        # Rörelse
        self.angle += self.speed
        if self.angle > 350 or self.angle < 190:
            self.speed = -self.speed
            self.angle += self.speed

        # Skjut med space
        if keys[pygame.K_SPACE]:
            self.shoot()

        # Uppdatera skotten
        for bullet in self.bullets:
            bullet.update()

        # Städa upp döda skott
        self.bullets = [bullet for bullet in self.bullets if bullet.is_alive()]

    def shoot(self):
        """Skjut ett skott!"""
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.fire_delay:
            self.last_shot = now
            # Skottets position är spelarens position + kanonens längd
            bullet_position = self.position + pygame.Vector2.from_polar(
                (self.cannon_size, self.angle)
            )
            bullet_velocity = pygame.Vector2.from_polar((self.bullet_speed, self.angle))
            # Skapa ett nytt skott och lägg till det i listan
            bullet = Bullet(self.bounds, bullet_position, bullet_velocity)
            self.bullets.append(bullet)

    def draw(self, screen):
        """Rita ut spelaren på skärmen."""
        # Rita kanontornet
        # Här utnyttjar vi att pygame.draw.circle kan rita kvadranter av cirklar
        pygame.draw.circle(
            screen,
            "blue",
            self.position,
            self.size,
            draw_top_left=True,
            draw_top_right=True,
        )

        # Rita pipan som en polygon som vi roterar till rätt vinkel
        points = [
            self.position + pygame.Vector2(40, 5).rotate(self.angle),
            self.position + pygame.Vector2(40, -5).rotate(self.angle),
            self.position + pygame.Vector2(70, -5).rotate(self.angle),
            self.position + pygame.Vector2(70, 5).rotate(self.angle),
        ]
        pygame.draw.polygon(screen, "blue", points)

        # Rita ut skotten
        for bullet in self.bullets:
            bullet.draw(screen)

    def get_rect(self):
        """Returnerar spelarens hit box"""
        return pygame.Rect(
            self.position - (self.size, self.size), (self.size * 2, self.size * 2)
        )

    def check_collisions(self, candies):
        """Kontrollerar om spelaren kolliderar med andra objekt
        och sköter logiken för vad som händer vid kollisioner."""
ß