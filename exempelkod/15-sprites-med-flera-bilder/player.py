import pygame

"""HÄR ÄR DET NYTT"""
# Saker som har tagits bort i klassen
    # is_alive attributet (det finns nämligen ett liknande inbyggt i Sprite-klassen)
    # metoden draw() är borta, då det sköts av logik i bla Sprite-klassen
    # metoden get_rect() är borta, då det behöver vara ett attribut istället på grund av hur Sprite-klassen fungerar

class Player(pygame.sprite.Sprite): # spelarklassen ärver av klassen Sprite från modulen sprite
    # Varje klass som är barn till Sprite-klassen behöver ha två attribut, ett self.image och ett self.rect
    def __init__(self, x=100, y=100):
        super().__init__() # initialiserar förälderklassens attribut och metoder
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.speed = 5
        
        # Ladda från ett spritesheet
        image = pygame.image.load("boy.png")
        self.img_left = image.subsurface((0,0,64,64))
        self.img_up = image.subsurface((64,0,64,64))
        self.img_down = image.subsurface((128,0,64,64))
        self.img_right = image.subsurface((196,0,64,64))
        
        # Välj valfri bild att starta med för att initialisera attributet
        self.image = self.img_up

        """HÄR ÄR DET NYTT"""
        self.rect = image.get_rect(topleft=(x,y)) # ett attribut som är hitbox
        # Vi utgår här ifrån bilden och talar om att vi vill ha top-left som utgångspunkt (går att ha center istället om man vill)


    def update(self, keys):
        self.dx = 0
        self.dy = 0

        if keys[pygame.K_LEFT]:
            self.dx = -1
            self.image = self.img_left
        elif keys[pygame.K_RIGHT]:
            self.dx = 1
            self.image = self.img_right
        elif keys[pygame.K_UP]:
            self.dy = -1
            self.image = self.img_up
        elif keys[pygame.K_DOWN]:
            self.dy = 1
            self.image = self.img_down
          
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

        """HÄR ÄR DET NYTT"""
        # Här ser vi till att potitionen för hitboxen också uppdateras när spelaren flyttas
        self.rect.topleft = (self.x, self.y)
    
