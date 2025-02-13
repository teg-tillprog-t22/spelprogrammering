## TillProg Spelprogrammering VT25

[⬅️ Gå tillbaka till startsidan](../../README.md)

👾 Gå till koden: [main.py](main.py) | [enemy.py](enemy.py) | [player.py](player.py)

## Patrullerande fiender

Här lägger vi till **patrullerande fiender** i spelet. En fiende rör sig inom skärmens område och vänder när den når kanten. Koden är uppdelad i tre filer:

- **`main.py`**: Huvudloopen; skapar spelare och fiender, uppdaterar dem och ritar dem.
- **`enemy.py`**: Innehåller klassen `Enemy` med logik för rörelse och livscykel.
- **`player.py`**: Innehåller klassen `Player`, här i en extremt enkel version som bara ritas ut men kan inte styras eller röra sig.

---

### 1. Fiender som patrullerar (`Enemy`-klassen)

```python
    def update(self):
        if self.is_alive():
            self.position += self.velocity
            if not self.bounds.contains(self.get_rect()):
                self.velocity = -self.velocity
                self.position += self.velocity
```

- **Attribut**: 
  - `position`: Fiendens nuvarande koordinater (Vector2).  
  - `velocity`: Hastighet (Vector2).  
  - `bounds`: Rektangel som anger spelplanens område.  
  - `state`: Indikerar om fienden är `ALIVE` eller `DEAD`.  

- **Patrull-logik**:
  - Fienden rör sig med `velocity` för varje uppdatering.
  - Om `self.get_rect()` ligger utanför `bounds`, **vänds** hastighetsvektorn med `self.velocity = -self.velocity` och fienden flyttas tillbaka till tidigare position.

- **Livscykel**: 
  - `die()` sätter `state` till `DEAD`.  
  - `is_alive()` returnerar `True` om fienden ska vara kvar i spelet.  
  - I huvudloopen städar vi bort döda fiender.

---

### 2. Huvudloopen (`main.py`)

```python
enemies = [
    Enemy(bounds, (20, 100), (1, 0)),  # Rör sig höger
    Enemy(bounds, (780, 200), (-1, 0)) # Rör sig vänster
]
```
- **Startvärden** för fiender: Position `(x, y)` och en hastighet `(1,0)` eller `(-1,0)` gör att de rör sig horisontellt.

- **Uppdatering**: 
  ```python
  player.update(keys)
  for enemy in enemies:
      enemy.update()
  ```
- **Borttagning** av fiender:  
  ```python
  enemies = [enemy for enemy in enemies if enemy.is_alive()]
  ```
- **Rita**:  
  ```python
  screen.fill("black")  
  for enemy in enemies:
      enemy.draw(screen)
  player.draw(screen)
  ```

Strukturen gör det enkelt att lägga till fler fiender eller ge dem olika startpositioner och hastigheter. För andra typer av rörelser eller logik så måste koden utökas eller skrivas om.
