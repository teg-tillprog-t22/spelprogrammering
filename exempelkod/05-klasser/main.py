from enum import Enum

# En enkel klass som kallas Player
class Player:
    # __init__ är en anropas när ett nytt objekt skapas
    def __init__(self, name):
        self.name = name  # attribut: spelarens namn
        self.x = 0        # attribut: x-koordinat
        self.y = 0        # attribut: y-koordinat
        self.score = 0    # attribut: poäng

    # En metod som flyttar spelare en givet antal steg
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    # En metod som interagerar med godisobjektet
    def eat_candy(self, candy):
        if candy.is_active():
            candy.eat()         # Godiset hanterar sitt eget tillstånd
            self.score += 100   # Öka poängen
            print(f"{self.name} har nu {self.score} poäng.")
        else:
            print(f"{self.name} hittade ingen godis att äta.")


# Skapa en enum för godisets tillstånd
class CandyState(Enum):
    ACTIVE = 1
    EATEN = 2

class Candy:
    def __init__(self, color):
        self.color = color
        self.state = CandyState.ACTIVE

    # Simulera att godiset blir uppätet
    def eat(self):
        if self.state == CandyState.ACTIVE:
            self.state = CandyState.EATEN
            print(f"En {self.color} godis blev uppäten!")
        else:
            print("Den här godisbiten är redan uppäten.")

    def is_active(self):
        return self.state == CandyState.ACTIVE

# Huvudfunktionen
def main():
    # Skapa en spelare och några godisar
    player = Player("Micke")
    candies = [Candy("röd"), Candy("blå"), Candy("grön")]

    # Simulate the player moving and eating candies:
    player.move(2, 3)
    for candy in candies:
        player.eat_candy(candy)

if __name__ == '__main__':
    main()
