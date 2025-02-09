## TillProg Spelprogrammering VT25

[⬅️ Gå tillbaka till startsidan](../../README.md)

👾 Gå till koden: [main.py](main.py) | [player.py](player.py)

## Kanoner och skott

I detta exempel lägger vi till:

1. **Skott (Bullet-objekt)** – hur de skapas, uppdateras och “dör” (tas bort).  
2. **Vektor-operationer** – hur spelarens kanonvinkel och skottets position/hastighet beräknas med `Vector2.from_polar`.  
3. **Rita halvcirklar** med `pygame.draw.circle(..., draw_top_left=True, ...)` för att illustrera kanontornet, och rita kanonröret som en linje.

Koden finns i två filer:

- `main.py` hanterar spel-loopen, skapar en spelare, ritar bakgrund precis som vanligt
- `player.py` innehåller både klasserna `Player` och `Bullet`. Spelarobjektet innehåller en lista med skott-objekt som uppdateras och ritas tillsammans med spelaren.

---

### 1. Skottens livscykel (klassen `Bullet`)

```python
    def update(self):
        self.position += self.velocity
        if not self.bounds.collidepoint(self.position):
            self.die()

    def die(self):
        self.state = Bullet.DEAD

    def is_alive(self):
        return self.state == Bullet.ALIVE
```

`update()` flyttar skottet med sin `velocity`.

Skottet vet storleken på spelytan (från `bounds` i `__init__`). För att se om skottet fortfarande är kvar inom spelytan används metoden `collidepoint()` som fungerar som `colliderect()` men tittar på kollision med en enda punkt.

Om skottet lämnat skärmen blir `not self.bounds.collidepoint(...)` lika med `False` och `die()` anropas (som markerar det som **DEAD**.)

I `Player.update()` filteras döda skott bort (med list comprehension):

```python
self.bullets = [bullet for bullet in self.bullets if bullet.is_alive()]
```

Detta förhindrar att vi behöver uppdatera eller försöka rita skott som är utanför skärmen.

Att låta skotten hanteras av spelarobjektet är ett *val* vi gör. I ett större spel
hade det kanske varit naturligare att skapa skotten utanför spelaren. Antingen i huvudloopen eller i en
särskild spelklass (typ ett `GameContext`). Men här funkar det fint att låta skotten *tillhöra* spelaren.

---

### 2. Skapa skott med `Vector2.from_polar()`

Kanonen har en **vinkel** `self.angle` samt en **längd** `self.cannon_size`. När man trycker på *mellanslag* anropas `shoot()`. Vinkeln uppdateras automatiskt över tid, så att kanonen rör sig fram och tillbaka
utan att användaren gör något.

```python
bullet_position = self.position + pygame.Vector2.from_polar((self.cannon_size, self.angle))
bullet_velocity = pygame.Vector2.from_polar((self.bullet_speed, self.angle))
```

`Vector2.from_polar((r, v))` skapar en vektor med längd `r` och vinkel `v` (i grader). Vi behöver inte själva räkna med cos och sin utan pygame löser det. Notera de dubbla parenteserna - from_polar tar en tuple som argument.

När skottet är skapat så läggs det i en lista av skott så att det uppdateras och ritas tillsammans
med alla andra skott.

---

### 3. Rita kanontorn och kanonrör

I `Player.draw()` finns två detaljer som är lite nya:

1. **Halvcirkel** för kanontornet:
   ```python
   pygame.draw.circle(
       screen,
       "blue",
       self.position,
       self.size,
       draw_top_left=True,
       draw_top_right=True,
   )
   ```
   - Med `draw_top_left=True` och `draw_top_right=True` ritas bara **övre** halvan av cirkeln på *båda sidor*, vilket ger en halvcirkel. (Att rita fyllda cirklar mellan godtyckliga vinklar är däremot pygame inte bra på.)
   - Eftersom `self.position` ligger nära botten av skärmen, ser det ut som ett halvt “torn” på marken.

2. **Kanonrör** som en linje:
   ```python
   cannon_start = self.position + pygame.Vector2.from_polar((40, self.angle))
   cannon_end = self.position + pygame.Vector2.from_polar((70, self.angle))
   pygame.draw.line(screen, "blue", cannon_start, cannon_end, 10)
   ```
   - Start- och slutpunkt bestäms via `from_polar`, baserat på samma vinkel.  
   - Linjens tjocklek sätts till 10 pixlar.

---

### Sammanfattning

- **Skott** skapas genom att vi räknar ut startposition (i toppen av kanonen) och hastighetsvektor med `from_polar`.
- **Uppdatering** och “död” sköts i `Bullet`. `Player` ansvarar för att ta bort dem när de inte längre "lever". Ungefär som det fungerade när vi hade godis som togs bort i huvudloopen.
- **Kanontorn** ritas som en **halvcirkel**.
- **Kanonröret** är en linje mellan två roterade koordinater, vilket gör att det pekar i samma riktning som skottet.

Strukturen håller koden relativt enkel och separerar mellan **spelarens logik** (vilka skott som finns, när de skjuts) och **skottets egen logik** (hur det rör sig och när det dör).
