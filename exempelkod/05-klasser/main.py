# En enkel klass som kallas Player
class Player:
    # __init__ är en anropas när ett nytt objekt skapas
    def __init__(self, name):
        self.name = name  # attribut: spelarens namn
        self.x = 0        # attribut: x-koordinat
        self.y = 0        # attribut: y-koordinat
        self.score = 0    # attribut: poäng

# Skapa en instance (ett objekt) av klassen Player
player1 = Player("Micke")
print(f"{player1.name} har position ({player1.x}, {player1.y}) och poäng {player1.score}.")
