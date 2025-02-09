import pygame

class Player:
    """
    Representerar spelaren
    """

    def __init__(self, width, height):
        """
        Initialisera spelarens attribut med startvärden 
        """
        self.position = pygame.Vector2(width//2, height//2)
        self.velocity = pygame.Vector2(3, 0)
        self.size = 20      # Storlek i pixlar
        self.points = 0
        self.width = width
        self.height = height

    def update(self, keys):
        """
        Uppdatera spelarens position och tillstånd
        Reagera på knapptryckningar
        """
        # Piltangenterna används för att förändra spelarens
        # riktining med 1/100 varv
        if keys[pygame.K_LEFT]:
            self.velocity.rotate_ip(-5)
        if keys[pygame.K_RIGHT]:
            self.velocity.rotate_ip(5)

        # Beräkna nya x från förflyttningen
        self.position += self.velocity

        # Kontrollera om de nya koordinaterna går utanför kanten
        # på skärmen

        # x-led
        if self.position.x > self.width-self.size or self.position.x < self.size:
            self.velocity.reflect_ip(pygame.Vector2(1,0))

        # y-led
        if self.position.y > self.height-self.size or self.position.y < self.size:
            self.velocity.reflect_ip(pygame.Vector2(0,1))

    def draw(self, screen):
        """
        Rita ut spelaren på skärmen.
        """
        now = pygame.time.get_ticks()
        # Rita spelarens kropp som en cirkel
        pygame.draw.circle(screen, "yellow", self.position, self.size)
        # Och lägg till ett streck från origo till cirkelns
        # kant för att visa riktningen
        endpos = self.position + self.velocity.normalize()*self.size
        pygame.draw.line(screen, "black", self.position, endpos, 2)

    def get_rect(self):
        """Returnerar spelarens hit box"""
        return pygame.Rect(self.position-(self.size, self.size), (self.size*2, self.size*2)) 

    def check_collisions(self, candies):
        """
        Kontrollerar om spelaren kolliderar med andra objekt
        och sköter logiken för vad som händer vid kollisioner
        """
        for candy in candies:
            if candy.is_active() and self.get_rect().colliderect(candy.get_rect()):
                candy.die()
                self.points += 100

