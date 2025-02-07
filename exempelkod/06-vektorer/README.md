## TillProg Spelprogrammering VT25

[⬅️ Gå tillbaka till startsidan](../../README.md)

👾 Gå till koden: [main.py](main.py) | [player.py](player.py) | [candy.py](candy.py)

## Vektorer och moduluppdelning

I detta exempel ersätter vi många av våra vanliga koordinatvariabler och trigonometriska beräkningar med klassen `pygame.Vector2` (2 som i tvådimensionell). Dessutom delar vi upp koden i tre filer:  
- **`main.py`** – Hanterar spel-loopen och sköter övergripande flöde.  
- **`player.py`** – Innehåller klassen `Player`.  
- **`candy.py`** – Innehåller klassen `Candy`.  

### 1. Varför dela upp koden i olika filer?

När spelet växer är det ofta bra att dela upp det i flera filer (moduler). Varje fil kan fokusera på en viss del av spelet, vilket gör koden mer lättläst och lättare att underhålla. Det går också lättare att hitta rätt kod.

- **`main.py`** har ett enda ansvar: att starta spelet och hålla i huvudloopen.  
- **`player.py`** innehåller all logik och rendering för spelarens rörelse, poäng etc.  
- **`candy.py`** definierar hur godiset fungerar – tillstånd (enum), utseende och “dödsprocess”.

Genom att importera de moduler vi behöver (`from player import Player` och `from candy import Candy`) får huvudfilen bara de klasser den behöver.

---

### 2. Användning av `pygame.Vector2`

`pygame.Vector2` är en **klass** som representerar en 2D-vektor med x- och y-värde. I `player.py` ser du exempel:

```python
self.position = pygame.Vector2(width//2, height//2)
self.velocity = pygame.Vector2(3, 0)
```

Istället för att hantera `x` och `y` separat (och använda trigonometri för rotationer och riktning), kan vi nu använda `Vector2`-metoder:

- **`rotate_ip(±vinkel)`**: Roterar vektorn (här hastigheten) in-place med angiven gradtal.  
- **`reflect_ip(...)`**: Studsar mot en normalvektor, exempelvis `(1,0)` för en vägg i x-led.  
- **Addition, subtraktion**: `self.position += self.velocity` uppdaterar enkelt positionen.

#### Fördelar
1. **Renare kod**: Vi slipper manuella beräkningar med `cos` och `sin` för rotation.  
2. **Inbyggda hjälpmetoder**: T.ex. `normalize()` och `reflect_ip()` för att underlätta beräkningar.  
3. **Mindre risk för misstag** kring trigonometriska formler.

#### Nackdelar
1. **Abstraktion**: En del av logiken (t.ex. hur rotationen fungerar) “göms” i klassen `Vector2`. Man får lita på att Pygames implementering är korrekt.  
2. **Mindre “manuell” träning** i att använda matematiska formler för rotationer och studsar. Trist, visst?

---

### 3. Exempel på reflektion och rotation

I `Player.update()` ersätter vi tidigare trigonometriska operationer med `rotate_ip` och `reflect_ip`:

```python
if keys[pygame.K_LEFT]:
    self.velocity.rotate_ip(-5)
if keys[pygame.K_RIGHT]:
    self.velocity.rotate_ip(5)

self.position += self.velocity

if self.position.x > self.width - self.size or self.position.x < self.size:
    self.velocity.reflect_ip(pygame.Vector2(1, 0))
if self.position.y > self.height - self.size or self.position.y < self.size:
    self.velocity.reflect_ip(pygame.Vector2(0, 1))
```

- **Rotation**: `rotate_ip(-5)` vrider hastighetsvektorn 5 grader medurs.  
- **Reflektion**: `reflect_ip(pygame.Vector2(1,0))` ändrar hastighetsvektorn så att den studsar “spegelvänt” mot en vertikal vägg.

---

### 4. Huvudfilen `main.py`

I `main.py` har vi fortfarande en **huvudloop** som:
1. Hanterar tid och events.  
2. Uppdaterar objekt (spelare, godisar).  
3. Kontrollerar kollisioner.  
4. Ritar allt på skärmen.  

Skillnaden är att spelaren och godiset finns i egna filer, vilket gör koden mer överblickbar.

---

### Sammanfattning

1. **Moduluppdelning**: Genom att ha `main.py`, `player.py` och `candy.py` blir koden lättare att underhålla och förstå.  
2. **`pygame.Vector2`** gör att vi slipper mycket egen trigonometri. Rotationer och studsar kan hanteras med inbyggda metoder, vilket ger renare kod.  
3. Du **vinner** tid och tydlighet, men **förlorar** en del direkt kontroll och förståelse för underliggande matematik.  

Det är fortfarande **samma principer** för spel-loopen, kollisioner och rendering – men nu har vi bättre stöd i vektoroperationer och en tydligare kodstruktur med flera filer.
