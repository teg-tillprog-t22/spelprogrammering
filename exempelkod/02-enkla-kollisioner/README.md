## TillProg Spelprogrammering VT25
[⬅️ Gå tillbaka till startsidan](../../README.md)

[👾 Gå till koden](main.py)

### Kollisioner och objektets livscykel

I detta exempel visar vi hur man kan hantera kollisioner mellan spelare och andra objekt (t.ex. godisar) i ett Pygame-baserat spel. Vi fokuserar på följande aspekter:

1. **Olika typer av kollisioner** (rektangulära, cirkulära, kantdetektering, "pixel perfect").  
2. **Ansvarsfördelning** (spelaren kontrollerar sina kollisioner med andra objekt)
3. **Hit boxes i detalj** (modellera kollisioner med överlappande rektanglar).
3. **Objektlivscykel** med hjälp av `is_alive()` och `die()` för säkert borttagande ur listor.  
4. **Edge detection** för enkel kollision med skärmens kanter, inklusive studslogik.  

---

### Spelloopen i korthet

Vi har en liknande struktur som i föregående exempel, med en **huvudloop** (`while running:`) där vi:

1. **Flyttar fram tid/frame** via `dt = clock.tick(FPS)`.  
2. **Hanterar events** (t.ex. stänga fönstret).  
3. **Uppdaterar spelvärlden** (spelare, fiender, belöningar) inklusive kollisionskontroll.  
4. **Ritar spelvärlden** och kallar på `pygame.display.flip()`.

---

### 1. Olika typer av kollisioner

- **Hitbox (rektangulär)**  
  Med `pygame.Rect` och `.colliderect()` kan vi enkelt kolla om två rektanglar överlappar.  
- **Cirkulär kollision**  
  Bygger på avståndsberäkning med Pythagoras sats. Visas här inte i koden men är ett alternativ.  
- **Edge detection**  
  I koden låter vi spelaren studsa mot skärmens kanter genom att justera `self.direction`.  
- **Pixel-perfect collision**  
  Avancerat exempel som kräver färginformation per pixel. Används sällan i små spel men kan vara bra att känna till.

---

### 2. Ansvarsfördelning: Spelaren kollar kollisioner

> Som tumregel är det enklast att låta spelaren själv kontrollera alla kollisioner som rör spelaren.

I metoden `check_collisions` (inne i `Player`-klassen) kallas godiset för “uppätet” om `colliderect` returnerar `True`, varpå `Candy`-objektet får utföra `die()`.  
På så sätt är huvudloopen renare, och ansvaret för spelarens kollisioner ligger i spelarens kod, medan ansvaret för vad som händer med godiset ligger i godisets kod (t ex en "dödsanimering").

Om det finns många godisar i spelet låter vi spelaren kontrollera kollision med varje enskilt objekt i tur och ordning.

---

### 3. Hantera borttagning av objekt

- Vi använder `Candy.State` för att avgöra om en godis är **ACTIVE**, **DYING** eller **DEAD**.  
- Metoden `is_alive()` anger om objektet fortfarande ska finnas i spelvärlden.  
- I huvudloopen skapar vi en ny lista  för att städa bort döda godisar på ett säkert sätt (efter att vi uppdaterat allt annat men innan vi ritar om skärmen).

Detta är ett vanligt mönster för att undvika fel som kan uppstå om man tar bort element direkt ur en lista man loopar igenom.

---

### 4. Kontrollera kollisioner med rektanglar

En vanlig metod för kollisioner i Pygame är att använda **rektanglar** (s.k. “hit boxes”). Om två rektanglar överlappar varandra, betraktas det som en kollision. Själva kollisionskontrollen sker via pygame-metoden `colliderect()`, som returnerar `True` om rektanglarna överlappar och annars `False`.

Ett typiskt flöde är:

1. **Skapa rektanglar**: Varje spelobjekt har en egen metod `get_rect()` som returnerar en `pygame.Rect` som utgör det objektets hit box.
2. **Kolla kollision**: Anropa `colliderect()` på ena objektets rektangel med den andra objektets rektangel som argument.

```python
# Anta att vi har två objekt, player och candy, där båda har en get_rect()-metod.
player_rect = player.get_rect()
candy_rect = candy.get_rect()

if player_rect.colliderect(candy_rect):
    # Om rektanglarna överlappar, gör någonting...
    candy.die()
```

I exemplet ovan är `get_rect()` implementerad så här:

```python
def get_rect(self):
    return pygame.Rect(
        self.x - self.size, 
        self.y - self.size, 
        self.size * 2, 
        self.size * 2
    )
```

Här tolkar vi spelarens position `(x, y)` som mittpunkten i en cirkel, men för kollisionskontrollen använder vi en **kvadratisk** rektangel (där bredden och höjden är `2 * size`). Denna förenklade “hitbox” är vanlig eftersom den är lätt att arbeta med och räcker långt för enklare 2D-spel.

---

### 5. Edge detection och studs

Spelaren kollar själv om den lämnar skärmen:

```python
if self.x > WIDTH-self.size or self.x < self.size:
    self.direction = pi - self.direction
if self.y > HEIGHT-self.size or self.y < self.size:
    self.direction = -self.direction
```

- När en studs sker i x-led, vänds vinkeln enligt \(\pi - \text{vinkel}\).  
- I y-led multipliceras vinkeln med \(-1\).  
- Det ger en illusion av att spelaren studsar mot väggen.

---

### Sammanfattning

I denna kod byggde vi vidare på spelloopen genom att:

1. Införa **kollisionshantering** med `colliderect()`.  
2. Ge objekten en **livscykel** (`ACTIVE`, `DYING`, `DEAD`) och säkert ta bort dem ur listor.  
3. Implementera **edge detection** för att spelaren inte ska försvinna utanför skärmen.

**Nästa steg** kan vara att:
- Lägga till cirkulär kollision om objekten är runda och du vill ha mer exakta beräkningar.  
- Införa fiender med mer avancerad kollisionslogik.  
- Skapa animation när godiset “dör” istället för att tas bort direkt.

Med denna struktur är det relativt enkelt att utöka spelet med fler typer av objekt och avancerade effekter utan att huvudloopen blir för rörig.

---

> **Tips**: Vid större projekt kan man använda en “Collision Manager”-klass som itererar över alla objekt och sköter kollisioner. Men för enklare spel räcker det ofta långt att låta spelaren (och andra större objekt) själva kontrollera vad de kolliderar med.

