## Övningsuppgifter – spelprogrammering

### Förberedelser
För de uppgifter som kräver programmering nedan är det mycket användbart att ha grunden till en program-struktur tillgänglig. På så sätt kan du både lösa den begränsade uppgiften som finns beskriven samtidigt som du har möjlighet att testa koden du skrivit.

Ett sätt att göra en sån struktur är att ta något av exempelprogrammen och ta bort all kod förutom den grundläggande.
Kopiera sedan den koden till en separat mapp och utgå från den
när du löser en uppgift.

Det är också smidigt att ha en enkla klasser `Player` och `Candy`
tillgängliga. Gör det till en övning att skriva dem.

--- 

### Uppgift 1: Initialisering
a.) Vad händer om vi glömmer att anropa `pygame.init()` i ett Pygame-program?  

--- 

### Uppgift 2: clock.tick()
a.) Beskriv vad kommandot `dt = clock.tick(60)` gör i Pygame. Förklara vad argumentet till metoden innebär och vad returvärdet kan användas till. Vilket annat begrepp kan vi använda för `dt`?

---

#### Lösning:

- `clock.tick(60)` begränsar spelets uppdateringsfrekvens till 60 FPS (frames eller bilder per sekund).
- Returvärdet är tiden i millisekunder som har gått sedan förra anropet.
- Detta returvärde kan användas för att göra rörelser och animationer oberoende av FPS, genom att skala objektets hastighet proportionellt mot den faktiska tid som har gått mellan frames.
- Utan detta riskerar spelet  att gå snabbare eller långsammare beroende på datorns prestanda, men genom att använda `dt` kan vi hålla en jämn hastighet oavsett FPS.
- Vi använder ibland begreppet **deltatime**.

---

### Uppgift 3: Initialisering

Skriv en minimal kod-snutt

   - Initialiserar pygame
   - Skapar ett fönster med bredd `200` och höjd `300`.
   - Fyller bakgrunden med en valfri färg.
   - Visar fönstret i 5 sekunder innan det stängs.
   - Stänger ner pygame

Använd `time.sleep()` för en blockerande paus.

---

### Uppgift 4: Ordning i huvudloopen
Sortera dessa steg i rätt ordning i en huvudloop:
- Rensa ut objekt som inte används
- Uppdatera objektens positioner och tillstånd
- Rita ut objekt
- Hantera event
- Växla källa för bilden på skärmen
- Hantera kollisioner
- Uppdatera klockan och spara deltatiden

---

### Uppgift 5: Rektanglar i Pygame
I Pygame har spelobjekt ofta ett attribut `rect` eller en metod `get_rect()`.

a.) Förklara varför och vad en sådan metod returnerar.

b.) Vilken information/vilka värden behövs för att skapa en sådan rect?

---

### Uppgift 6: Skillnad på `update()` och `draw()`

Förklara varför vi delar upp `update()` och `draw()` i olika metoder. Vilken funktionalitet bör respektive metod innehålla?

---

#### Lösning:
- `update()` ansvarar för att uppdatera objektets tillstånd, t.ex. position och hastighet.
- `draw()` ansvarar endast för att rita objektet på skärmen.
- Separationen gör koden renare och mer flexibel.
- Enklare felsökning då logiken är separerad från grafiken
- Genom att uppdatera spellogiken med både förflyttningar och kollisionser innan något ritas ut på skärmen undviks att objekt ritas felaktigt eller i onödan.

---

### Uppgift 7: Samma fart, olika riktning
a.) Hur kan vi göra för att ett spelobjekt ska röra sig med samma fart oavsett riktning?

b.) Skriv en kodsnutt för att en fiende på en viss position ska röra sig mot spelaren med konstant fart.

---

#### Lösning:
a.) För att ett objekt ska röra sig med konstant hastighet oavsett riktning, kan vi använda förändringen i x-led (`dx`) och y-led (`dy`). Dessa komponenter utgör den totala rörelsen. För att hålla hastigheten konstant, delar vi `dx` och `dy` med vektorns längd, vilket normaliserar rörelsen. Därefter kan vi multiplicera med den fart som vi önskar.

2. Kodsnutten kan t.ex. skrivas:

```python
direction = player.position - self.position
if direction.length() > 0:
    direction = direction.normalize()
    self.position += direction * self.speed
```

eller

```python
dx = player.x - self.x
dy = player.y - self.y
distance = (dx**2 + dy**2)**0.5
if distance > 0:
    self.x += (dx / distance) * self.speed
    self.y += (dy / distance) * self.speed
```

---

### Uppgift 8: Rensa döda objekt


a.) **Varför** vill vi rensa bort döda objekt (t.ex. uppätna godisar eller döda fiender)?

b.) Vad är det bästa sättet att ta bort flera objekt från en lista utan att orsaka buggar?

c.) Skriv på papper - korrekt eller nästan korrekt - en kodsnutt för att ta bort godisar som inte längre är aktiva i ett spel. Objekt av klassen ``Candy`` har ett attribut `alive` som är `True` eller `False`.

---

#### Lösning:
Med list comprehension:
```python
candies = [c for c in candies if c.alive]
```

Utan list comprehension:
```python
new_candies = []
for c in candies:
    if c.alive:
        new_candies.append(c)
candies = new_candies
```

---

### Uppgift 9: Sortera huvudloopen
1. Nedan finns en osorterad huvudloop. Skriv om den i rätt ordning och lägg till kommentarer som avdelar de olika stegen.

```python
pygame.display.flip()
player.update()
clock.tick(60)
for enemy in enemies:
    enemy.draw(screen)
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
for enemy in enemies:
    enemy.update()
for candy in candies:
    candy.update()
player.draw(screen)
for candy in candies:
    candy.draw(screen)

```

#### Uppgift 10: Flytta objekt utanför skärmen
a.) Vad händer om ett objekt får koordinater utanför skärmens storlek i pygame?

b.) Skriv en metod wrap_around() som gör att ett objekt som går ut på höger sida av skärmen kommer in från vänster.

---

### Uppgift 11: Skapa en timer i spelet
a.) Hur kan vi skapa en timer i pygame som gör att en händelse inträffar var femte sekund?

b.) Skriv en kodsnutt där en fiende byter position var femte sekund med hjälp av `pygame.time.get_ticks()`.

---

#### Lösning:

```python
import pygame

class Enemy:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.last_update = pygame.time.get_ticks()
        self.interval = 5000  # 5 sekunder

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update > self.interval:
            self.position.x += 50  # Flytta fienden
            self.last_update = current_time
```

---


### Uppgift 12: Slumpmässig placering av objekt

a.) Hur kan vi placera ut objekt slumpmässigt i Pygame?

b.) Skapa en klass `Candy` där godisbitarna placeras på slumpmässiga koordinater vid start.

#### Lösning:

```python
import random

class Candy:
    def __init__(self, screen_width, screen_height):
        self.position = pygame.Vector2(random.randint(0, screen_width), random.randint(0, screen_height))
```

---

### Uppgift 13: Dynamiskt ändra hastighet

a.) Hur kan vi göra så att spelarens hastighet ökar över tid?

b.) Implementera funktionalitet i en `Player`-klass som ökar hastigheten var tionde sekund.

c.) Lägg funktionaliteten i en metod `increase_speed()` som anropas från `update()`

---

#### Lösning:

```python
class Player:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.speed = 2
        self.last_update = pygame.time.get_ticks()

    def update(self):
        # Dela upp i olika funktioner för att göra
        # koden lättare att läsa
        self.increase_speed()

        # Flytta spelaren
        self.position.x += self.speed

    def increase_speed(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update > 10000:  # 10 sekunder
            self.speed += 1
            self.last_update = current_time
```

---

### Uppgift 14: Förändra fiendens riktning vid kollision

a.) Hur kan vi få en fiende att byta riktning när den träffar en vägg?

b.) Implementera funktionalitet som gör att fienden vänder vid en viss gräns.

---

#### Lösning:
```python
class Enemy:
    def __init__(self, x, y, speed):
        self.position = pygame.Vector2(x, y)
        self.speed = pygame.Vector2(speed, 0)

    def update(self, screen_width):
        self.position += self.speed
        if self.position.x < 0 or self.position.x > screen_width:
            self.speed.x *= -1  # Byt riktning
```

---

### Uppgift 15: Låt spelaren skjuta projektiler
1. Skapa en `Bullet`-klass med en projektil som rör sig rakt uppåt. När den når toppen av skärmen skall den dö, dvs få statusen `is_alive=False`.

Anta att det är spelaren som skjuter projektiler.

1. **Var** i koden är det lämpligt att **skapa** projektiler?
1. **Hur** är det lämpligt att **lagra** dem?
1. **Var** i koden är det lämpligt att **rensa** ut döda projektiler?
1. **Hur** är det lämpligt att strukturera koden så att alla projektiler uppdateras och ritas?

---

#### Lösning:
```python
class Bullet:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.speed = 5
        self.alive = True

    def update(self):
        self.position.y -= self.speed
        if self.position.y < 0:
            self.alive = False
```


### Uppgift 17: Flytta en fiende längs en bana

a.) Hur kan vi få en fiende att röra sig fram och tillbaka längs en bana?

b.) Implementera en metod `patrol()` som gör att fienden rör sig mellan två punkter. Anropa metoden från `update()`.

c.) Kan du komma på några fördelar med att lägga funktionaliteten i egen metod och inte direkt i `update()`?

---

#### Lösning:
```python
class Enemy:
    def __init__(self, x, y, speed, left_limit, right_limit):
        self.position = pygame.Vector2(x, y)
        self.speed = speed
        self.left_limit = left_limit
        self.right_limit = right_limit
        self.direction = 1  # 1 = höger, -1 = vänster

    def patrol(self):
        self.position.x += self.speed * self.direction
        if self.position.x >= self.right_limit or self.position.x <= self.left_limit:
            self.direction *= -1  # Byt riktning
```


### Uppgift 18: Räkna antal godisar spelaren samlat
a.) Hur kan vi hålla koll på hur många godisar en spelare har samlat in?

b.) Lägg till ett `score`-attribut och en metod `collect_candy()` i klassen `Player`. Metoden  tar en lista med godisar, kolla kollisioner och ökar poängen. Du behöver bara skriva de relevanta delarna av konstruktorn metoden och kan anta att annan nödvändig funktionalitet finns tillgänglig.

---

#### Lösning:
```python
class Player:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.score = 0

    def collect_candy(self, candies):
        for candy in candies:
            if self.get_rect().colliderect(candy.get_rect()):
                self.score += 1
                candy.die()
```

### Uppgift 19: Låt en fiende jaga spelaren men hålla avstånd

a.) Hur kan vi få en fiende att jaga spelaren men aldrig komma närmare än 50 pixlar?

b.) Implementera funktionaliteten i metoden `update()`.

---

#### Lösning:
```python
class Enemy:
    def __init__(self, x, y, speed):
        self.position = pygame.Vector2(x, y)
        self.speed = speed

    def update(self, player):
        distance = self.position.distance_to(player.position)
        if distance > 50:
            direction = (player.position - self.position).normalize()
            self.position += direction * self.speed
```

### Uppgift 20: Styr hastigheten med tangenter**

a.) Hur kan vi ändra spelarens hastighet genom att hålla nere en knapp?

b.) Lägg till funktionalitet i en spelares `update()` som gör att spelaren rör sig snabbare om `pygame.K_LSHIFT` hålls ner.








Här är tio nya uppgifter med fokus på **teorifrågor och felsökning i begränsade kodexempel**:

---

### **Uppgift 21: Vad gör `pygame.display.flip()` och `pygame.display.update()`?**
1. Vad är skillnaden mellan `pygame.display.flip()` och `pygame.display.update()`?
2. När är det bättre att använda `update()` istället för `flip()`?

---

#### **Lösning:**
- `pygame.display.flip()` uppdaterar hela skärmen.
- `pygame.display.update()` kan uppdatera en specifik del av skärmen, vilket kan vara mer effektivt om bara vissa objekt förändras.

---

### **Uppgift 22: Varför händer inget?**
Vad är felet i följande kod? Förklara och rätta till det.

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))

while True:
    pygame.event.get()
    screen.fill((255, 255, 255))
```

---

#### **Lösning:**
- Programmet fryser eftersom det saknar **en avslutningsmekanism** och **uppdatering av skärmen**.
- Rättad version:

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    pygame.display.flip()
```

---

### **Uppgift 23: Vad gör denna kod?**
Vad kommer följande kod att skriva ut? Förklara varför.

```python
class GameObject:
    def __init__(self, x):
        self.x = x

obj1 = GameObject(10)
obj2 = obj1
obj2.x = 20

print(obj1.x)
```

---

#### **Lösning:**
```
20
```
- `obj2 = obj1` gör att **båda variablerna refererar till samma objekt**.
- Ändringar i `obj2` påverkar även `obj1`.

---

### **Uppgift 24: Vad händer om vi tar bort `self`?**
Vad är felet i följande kod?

```python
class Player:
    def __init__(x, y):
        x = x
        y = y
```

---

#### **Lösning:**
- Konstruktorn saknar **`self`** och lagrar inte värdena korrekt.
- Rättad version:

```python
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

---

### **Uppgift 25: Vad gör denna kod?**
Vad skrivs ut? Förklara.

```python
x = 5

def change_x():
    x = x + 1

change_x()
```

---

#### **Lösning:**
- Felet: `x = x + 1` försöker ändra `x`, men Python ser det som en **lokal variabel** och den är inte definierad innan den används.
- Rättad version:

```python
x = 5

def change_x():
    global x
    x = x + 1

change_x()
print(x)  # 6
```

---

### **Uppgift 26: Kollision fungerar inte – varför?**
Vad är felet i följande kod?

```python
class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)

    def check_collision(self, enemy):
        if self.rect == enemy.rect:
            print("Kollision!")
```

---

#### **Lösning:**
- `self.rect == enemy.rect` kontrollerar om **rektanglarna är exakt lika**, vilket är fel.
- Rätt version:

```python
def check_collision(self, enemy):
    if self.rect.colliderect(enemy.rect):
        print("Kollision!")
```
- `colliderect()` kollar **överlappning** istället för exakta värden.

---

### **Uppgift 27: Oändlig loop – varför?**
Vad är felet i följande kod?

```python
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
```

---

#### **Lösning:**
- `pygame.event.wait()` returnerar **bara ett event** i taget och kan fastna om inga event händer.
- Rättad version:

```python
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
```

---

### **Uppgift 28: Fienden rör sig inte – varför?**
Vad är felet i följande kod?

```python
class Enemy:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.speed = pygame.Vector2(2, 0)

    def update(self):
        position += self.speed
```

---

#### **Lösning:**
- Felet är att `position` inte refererar till `self.position`, så det skapas en **lokal variabel** istället för att ändra objektets position.
- Rättad version:

```python
def update(self):
    self.position += self.speed
```

---


### Uppgift: Skärminställningar

a.) Vad gör `pygame.display.set_mode((800, 600))`?

---

### Uppgift 33: Hur fungerar funktionerna för att rita

a.) Vilka argument behöver `pygame.draw.circle()`?

b.) Vilka argument behöver `pygame.draw.rect()`?

c.) Vilka argument behöver `pygame.draw.polygon()`?

d.) Vad returnerar de tre funktionerna?

---

### Uppgift: Vad händer om vi glömmer att flippa skärmen

a.) Varför måste vi anropa `pygame.display.flip()` varje varv i loopen?

b.) Vad händer om vi inte gör det?

---

### Uppgift: Hur fungerar det när vi kollar knapptryckningar

a.) Vad returnerar `pygame.key.get_pressed()`?

b.) Vad är skillnaden mellan att undersöka om en knapp tryckts ned genom att använda event-kön (t ex händelsen `pygame.KEYDOWN`) och att kolla `pygame.key.get_pressed()`?

---

### Uppgift: Vad är en hitbox?

1. Vad menas med en **hitbox** i spelprogrammering?

2. Varför använder vi rektanglar (`pygame.Rect`) för att representera hitboxar?

---

### Uppgift: Varför använda klasser i Pygame?

a.) Vilka fördelar finns med att använda klasser i spelprogrammering?

b.) Hur kan klasser hjälpa till att organisera spelets kod?

---

### Uppgift: Vad innebär begreppet "modularitet" i ett spelprojekt?

1. Hur kan vi uppnå modularitet i ett Pygame-spel?

2. Varför är modularitet viktigt när vi programmerar större projekt?

---

### Uppgift: Varför använda vektorer istället för enkel geometri?

a.) Vad är skillnaden mellan att räkna rörelser med `x, y`-koordinater och att använda `pygame.Vector2()`?

b.) Nämn en situation där vektorer gör det enklare att implementera spelrörelse.

---

### Uppgift: Hur fungerar kollisionshantering i Pygame?

a.) Vilka olika sätt kan vi använda för att upptäcka kollisioner mellan objekt?

b.) Hur fungerar `colliderect()`, `contains()` och `collidepoint()`?

---

### Uppgift: Vad menas med att en fiende "patrullerar"?

a.) Vad betyder det att en fiende patrullerar, jagar respektive flyr?

b.) Beskriv med ord hur du skulle implementera de olika varianterna i en `Enemy`-klass. Vilken information behöver du tillgång till?

---

### Uppgift: Vad är en spelloop och varför behövs den?

a.) Vad är en **spelloop** och varför behövs den i ett Pygame-spel?

b.) Vilka delar ingår vanligtvis i en spelloop och i vilken ordning bör de exekveras?

---

### Uppgift: Hur hanteras kollisioner mellan spelaren och fiender?

a.) Vem ansvarar lämpligen för att kontrollera kollisioner i ett mindre spel – huvudloopen eller enskilda objekt? Motivera ditt svar.

b.) Vad kan hända om vi kontrollerar kollisioner på fel plats i programmet?
