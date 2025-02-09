## TillProg Spelprogrammering VT25

[⬅️ Gå tillbaka till startsidan](../../README.md)

👾 Gå till koden: [main.py](main.py) | [player.py](player.py) | [starfield.py](starfield.py)

## Rymdskepp och stjärnhimmel

I detta exempel gör vi ett nytt stil på samma format som tidigare men med två nya idéer:

1. **Rotation av polygoner** – Vi ritar ett rymdskepp genom att rotera en uppsättning fördefinierade punkter med hjälp av `Vector2.rotate()`.  
2. **Stjärnhimmel** – Vi skapar en bakgrund genom att placera ut många “stjärnor” och uppdatera deras positioner i förhållande till spelarens rörelse.

Koden är uppdelad i flera filer:

- **`main.py`**  
  – Har huvudloopen och skapar ett `Player`-objekt.  
- **`player.py`**  
  – Innehåller klassen `Player` och en enkel klass `Bullet` (spelaren kan skjuta).  
- **`starfield.py`**  
  – Definierar hur en enskild “Star” och hela `StarField` hanteras.

---

### 1. Nytt i `player.py` – Rotera rymdskepp och simulera bakgrund

```python
SHIP_SHAPE = (
    (-20, 5),
    (-15, -10),
    (-10, 5),
    (0, -25),
    (10, 5),
    (15, -10),
    (20, 5),
)
```
Rymdskeppets “grundform” beskrivs som en serie koordinater i en **tuple**. Vi använder tuples för de är *immutable* - dvs inte går att mutera (ändra). Vi vill att formen skall vara en konsatnt.

Under spelet roteras sedan varje koordinat beroende på spelarens nuvarande vinkel. 

#### Rotation av polygonpunkter

```python
points = [
    self.position + pygame.Vector2(x, y).rotate(self.angle)
    for x, y in Player.SHIP_SHAPE
]
```
Att använda *list comprehensions* är smidigare och mer "pythonic" än att använda en vanlig loop även
om det skulle ha fungerat precis lika bra. Vi roterar alla punkter på samma sätt.

- **`pygame.Vector2(x, y).rotate(self.angle)`** sköter själva rotationen.  
- Vi lägger till spelarens nuvarande `position` för att placera polygonen på rätt ställe på skärmen.  
- På samma sätt beräknas brännarnas (eldstrålar) form om `K_UP` är nedtryckt.

#### Fiktiv bakgrundsrörelse

Skeppet är i praktiken stationärt i mitten, men genom att uppdatera stjärnornas position med **motsatt** hastighet (`-self.velocity`) skapar vi en illusion av att spelaren rör sig.  
```python
self.starfield.update(-self.velocity)
```
- Om spelaren t.ex. rör sig uppåt med vektor `(0, -1)`, uppdaterar vi stjärnor med `(0, +1)`.

---

### 2. Hantering av en “stjärnhimmel” (`starfield.py`)

För bakgrunden definieras två klasser:

1. **`Star`** – en enskild stjärna med en position, storlek och färg.  
2. **`StarField`** – en samling stjärnor, som kan ritas eller uppdateras i sin helhet.

```python
class StarField:
    def __init__(self, bounds, number_of_stars=100):
        self.bounds = pygame.Rect(bounds)
        self.stars = [Star(self.bounds) for _ in range(number_of_stars)]
```

- **`StarField`** skapar ett antal stjärnor inom en viss yta (`bounds`).  
- Varje **`Star`** ritas med en enkel `pygame.draw.circle`.  
- I `Star.update()`, kollar vi om stjärnan lämnar skärmen. Om så är fallet, lägger vi tillbaka den på motsatt sida för att ge en känsla av en oändlig stjärnhimmel.

Hanteringen av stjärnor som hamnar utanför skärmen hanteras på det här stället i koden:
```python
if not self.bounds.collidepoint(self.position):
    # Flytta stjärnan till motsatt sida ...
    ...
self.position += velocity
```

#### Fördelar med stjärnklass

- Lätt att byta utseende (storlek, färg) eller lägga till nya effekter (blinkande, fallande stjärnor).
- Enkel att utöka med “lager” av stjärnor med olika hastigheter (parallax-scrolling).

Det är inte självklart vilken logik för stjärnhimlen som ska ligga i stjärnfältsklassen och vilka som ska ligga i den enskilda stjärnans klass. Det det är ett **val** vi har gör. Det hade t ex gått lika bra att låta stjärnhimlen ansvara för att ta bort döda stjärnor och skapa nya t ex.

---

### 3. Sammanfattning

- **Polygonrotation** med `Vector2.rotate()` låter oss rita rymdskepp i valfri vinkel utan komplicerad trigonometrikod.  
- **Stjärnhimmel**: Vi flyttar stjärnor med samma, men motsatt, hastighet som spelaren för att skapa en illusion av flygning.  
- **Kodstruktur**: Att ha en separat modul för stjärnhimlen (`starfield.py`) gör det lätt att vidareutveckla, t.ex. med fler effekter eller mer komplex bakgrund.
