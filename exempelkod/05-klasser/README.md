## TillProg Spelprogrammering VT25

[⬅️ Gå tillbaka till startsidan](../../README.md)

[👾 Gå till koden](main.py)

[🖥️ Gå till presentationen från lektionen](https://docs.google.com/presentation/d/1PQ8bZSnIzOrrk81jQqsUr7nhtuTJOeXn2ij59O-wPII/edit?usp=sharing)

### Klasser och objektorienterad programmering (OOP)

I det här exemplet går vi stegvis igenom hur grunderna i att använda klasser, metoder, attribut och interaktion mellan objekt. Det som kallas objektorienterad programmering.


### 1. En klass är en ritning för objekt

En enkel klassdefinition kan se ut som nedan. Den beskriver vilken data (attribut) som klassen har har, samt hur ett objekt kan skapas.

Själva poängen med klasser är att data och funktionalitet som naturligt hör ihop kan hanteras tillsammans. Detta tänker vi på när vi väljer vilka klasser vi vill ha i vår kod, och vilka attribut och metoder som passar var.

När vi använder klassen så skapar vi **objekt**. Precis som vi kan bygga många hus från samma ritning kan vi göra många objekt av samma klass. Objekten delar vilken **typ** av data de innehåller, men deras faktiska **värden** skiljer sig åt. Vi kan till exempel ha två spelare `Player`, där den ena har namnet (t ex) Micke och den andra (t ex) Molle.

Den speciella variabeln `self` används inne i klassen för att referera till just det egna objektets värden.

```python
class Player:
    def __init__(self, name):
        self.name = name  # attribut: spelarens namn
        self.x = 0        # attribut: x-koordinat
        self.y = 0        # attribut: y-koordinat
        self.score = 0    # attribut: poäng
```

- `__init__` är en speciell metod (kallas konstruktorn) som anropas när man skapar ett nytt objekt.
- **Attribut** (exempelvis `self.x`) beskriver objektets data/tillstånd.

---

### 2. Metoder är funktioner i klassen

En **metod** är en funktion som definieras inne i klassen. Den kan ändra objektets tillstånd eller utföra andra uppgifter. Parametrar används för att skicka in data. Även här används `self` för att referera till och ändra det egna objektets attribut.

```python
def move(self, dx, dy):
    self.x += dx
    self.y += dy
```

- **Inkapsling**: Metoderna ändrar objektets egna attribut utan att utomstående kod behöver veta detaljerna.  
- **Parametrar**: `dx` och `dy` anger här hur långt objektet ska flyttas i x- och y-led. Metoden uppdaterar sedan objektets tillstånd.

---

### 3. Fler klasser – Enums och interna tillstånd

För att utveckla vårt exempel skapar vi ytterligare en klass. Här introduceras klassen `Candy`, en godis som spelaren kan äta.

Vi låter vårt godis ha en färg, och ett tillstånd som avgör om det är aktivt eller uppätet. Vi lagrar tillståndet i en enum som kan innehålla två värden.

```python
from enum import Enum

class CandyState(Enum):
    ACTIVE = 1
    EATEN = 2

class Candy:
    def __init__(self, color):
        self.color = color
        self.state = CandyState.ACTIVE

    def eat(self):
        if self.state == CandyState.ACTIVE:
            self.state = CandyState.EATEN
            print(f"En {self.color} godis blev uppäten!")
```

- **Enum**: `CandyState` tydliggör att godiset kan vara `ACTIVE` eller `EATEN`.  
- **Interna tillstånd**: `self.state` anger vilket läge godiset är i.

---

### 4. Interaktion mellan objekt

Spelarens klass kan nu anropa metoder i godiset:

```python
def eat_candy(self, candy):
    if candy.is_active():
        candy.eat()          # Anropar Candy-klassens metod
        self.score += 100    # Ändrar spelarens poäng
        print(f"{self.name} har nu {self.score} poäng.")
    else:
        print(f"{self.name} hittade ingen godis att äta.")
```

- **Interaktion**: Spelaren avgör om godiset är aktivt (`is_active()`), och om så är fallet kallas `candy.eat()`.  
- **Flera tillstånd uppdateras**: Både godiset (byter state) och spelarens poäng ändras.

Ofta är det att föredra att spelaren anropar en metod hos godiset när det ska "dö" (`candy.die()`) istället för att direkt sätta om attributet (`candy.state`). Koden hålls strukturerad genom att samla all logik som rör godiset i själva klassen `Candy`. 

---

### 5. Huvudfunktionen

Sätter vi ihop allt ovan till ett litet test kan det se ut så här:

```python
def main():
    player = Player("Micke")
    candies = [Candy("röd"), Candy("blå"), Candy("grön")]

    player.move(2, 3)
    for candy in candies:
        player.eat_candy(candy)

if __name__ == '__main__':
    main()
```

- **Skapa objekt**: En `Player` med namnet “Micke” och en lista av `Candy` i olika färger.  
- **Metodanrop**: Spelaren rör sig och äter godis. Vi kan följa utskrifterna i terminalen för att se hur poängen ökar.

---

### Sammanfattning

1. **Klasser** är ritningar för objekt (attribut och metoder).  
2. **Metoder** är funktioner i klassen som ändrar objektets tillstånd eller utför logik.  
3. **Fler klasser** ger oss olika objekt (t.ex. `Player` och `Candy`).  
4. **Interaktion** sker när ett objekt kallar metoder i ett annat.  
5. **Huvudfunktionen** knyter ihop alla delar och låter oss köra programmet.

Denna struktur är en grundsten i **objektorienterad programmering**. När du lägger till grafik, kollisioner och andra spelfunktioner ska du försöka tänka på samma sätt. Funktioner och data som hör ihop kan samlas i klasser och objekt. Den kognitiva belastningen att läsa koden blir mindre när man kan koncentrera sig på små bitar i taget.
