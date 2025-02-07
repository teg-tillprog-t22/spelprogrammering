## TillProg Spelprogrammering VT25
[⬅️ Gå tillbaka till startsidan](../../README.md)

[👾 Gå till koden](main.py)

### Enkel animering och `enum`-baserade tillstånd

I detta exempel utökar vi vårt spel med **enkel animering** när ett objekt (ett “godis”) håller på att försvinna (DYING). Vi använder en **enum** för att skilja på olika tillstånd, så att både logik och ritning beror på om godiset är **ACTIVE**, **DYING** eller **DEAD**.

---

### 1. Varför `enum`?

En **enum** (förkortning av *enumeration*/uppräkning) är ett sätt att skapa namngivna konstanter som hör ihop logiskt. Exempelvis kan vi definiera olika “states” för ett objekt: `ACTIVE`, `DYING` och `DEAD`. Det hjälper oss att:

1. **Göra koden mer läsbar**:  
   I stället för att använda “magiska siffror” som `1`, `2`, `3` har vi beskrivande ord som `ACTIVE`, `DYING`, `DEAD`.
2. **Förhindra fel**:  
   Det är svårare att råka stava fel eller använda fel nummer.  
3. **Hålla logiken samlad**:  
   Vi kan enkelt se vilka tillstånd som finns, och lägga till fler senare om spelet växer (t.ex. `SPAWNING` eller `HIDDEN`).

I Python skapar vi en enum genom att göra en klass som ärver (det har vi inte pratat om, men se syntaxen nedn) från `Enum`, t.ex.:
```python
class State(Enum):
    ACTIVE = 1
    DYING = 2
    DEAD = 3
```
Vi sätter godisets tillstånd i variabeln `self.state` till en av de namngivna konstanterna. Namnen kan sedan användas i koden för att styra både beteende (logik) och hur objektet ritas.

---

### 2. Översikt av “Dying”-animering

När spelaren äter ett godis kallas `candy.die()`, vilket sätter godiset i **DYING**-tillstånd:

```python
def die(self):
    self.state = Candy.State.DYING
    self.death_time = pygame.time.get_ticks()
```

Vi **återanvänder** attributet `death_time` för att veta när animeringen startar. I `Candy.update()` avgör vi när godiset ska övergå till **DEAD**, och i `Candy.draw()` ritar vi själva animationen:

```python
case Candy.State.DYING:
    time_since_death = now - self.death_time
    # Öka storleken med en pixel per 25 ms
    radius = self.size + time_since_death // 25
    # Rita ut godiset som en oifylld cirkel
    pygame.draw.circle(screen, self.color, (self.x, self.y), radius, 2)
```

På så vis blir **DYING**-tillståndet ett par sekunder långt innan objektet “försvinner” (går över till **DEAD**).

---

### 3. Förtydligad kod för `Candy.draw()`

Här är ett den relevanta koden som skiljer på ritlogiken för olika tillstånd. För enkelhets skull är koden som får godiset att blinka innan det försvinner borttaget.

```python
def draw(self, screen):
    now = pygame.time.get_ticks()
    match self.state:
        case Candy.State.ACTIVE:
            # Ritar ut godiset som en fylld cirkel
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

        case Candy.State.DYING:
            # Enkel “puff”-animering
            time_since_death = now - self.death_time
            radius = self.size + time_since_death // 25
            pygame.draw.circle(screen, self.color, (self.x, self.y), radius, 2)

        case Candy.State.DEAD:
            # Ritar inte alls
            pass
```

1. **ACTIVE**: Godiset ritas som en vanlig fylld cirkel. Extra blinkning (on/off) sista sekunden.  
2. **DYING**: Vi låter cirkeln växa under en kort tid, ritar den oifylld för “puff”-effekt.  
3. **DEAD**: Ritas inte alls.

---

### 4. Användning i huvudloopen

Huvudloopen ändras inte särskilt mycket från tidigare exempel. Den centrala idéen är att:

1. Varje godis uppdateras med `candy.update()` – där kollar vi **State**-logiken (om och när den ska övergå till `DEAD`).  
2. Vi **ritar** med `candy.draw(screen)` – där animeras den olika beroende på `ACTIVE`, `DYING` eller `DEAD`.  
3. När ett godis är **DEAD**, tas det bort i en städfas:  
   ```python
   candies = [c for c in candies if c.is_alive()]
   ```

---

### Sammanfattning

- **Enum** ger en tydligare struktur där varje tillstånd är ett namngivet värde.  
- **Animering** sköts enkelt genom att beräkna hur lång tid som gått sedan godiset gick in i DYING-tillståndet.  
- Huvudloopen förblir ren och hanterar bara städning och skapande av nya objekt.

Strukturen lägger grunden till mer avancerade animeringar och logik i spelet, utan att koden blir svåröverskådlig tack vare enum-baserade tillstånd.

> **Tips**: Testa olika/andra animeringsmetoder för `DYING`, till exempel  
> - Fadea ut färgen gradvis.  
> - Lägg till “skakning” eller partikeleffekter (svårare).  
