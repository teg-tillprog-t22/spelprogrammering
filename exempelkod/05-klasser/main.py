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

# Skapa en spelare och flytta hen
player1 = Player("Micke")
player1.move(5, -2) # Förflyttar 5 steg i x och -2 steg i y
print(f"{player1.name} har position ({player1.x}, {player1.y}) och poäng {player1.score}.")

# Skapa en godis och ät den
candy1 = Candy("röd")
print(f"Är godisbiten aktiv? {candy1.is_active()}")
candy1.eat()
print(f"Är godisbiten aktiv? {candy1.is_active()}")
