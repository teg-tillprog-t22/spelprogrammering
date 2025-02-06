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

# Skapa en spelare och flytta hen
player1 = Player("Micke")
player1.move(5, -2) # Förflyttar 5 steg i x och -2 steg i y
print(f"{player1.name} har position ({player1.x}, {player1.y}) och poäng {player1.score}.")
