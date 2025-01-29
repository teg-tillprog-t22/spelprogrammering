# Spelprogrammering

## Programstruktur

### Huvudloopen

```python
# Funktion som representerar en spelomgång
def play():
    # Initialisera spelvärlden

    running = True
    while running:
        # Flytta fram frame/tid

        # Hantera händelser/events

        # Uppdatera rörelser och spellogik

        # Rita ut spelvärlden

        # Flippa till den nya bilden
```

#### 1. Flytta fram tid/frame

Mellan varje varv i huvudloopen, dvs en frame, så kör vi kommandot

```python
while running:
    dt = pygame.clock.tick(FPS)
```

`FPS` (frames per sekund) är en konstant som vi definierar till att vara *maximal* framerate för spelet. 60 frames per sekund är en lämplig uppdateringsfrekvens som överenstämmer med många skärmars uppdateringshastighet.

Funktionen returnerar hur många millisekunder det har gått sedan föregående bildruta. Vi kallar detta för **deltatid**, ```dt```. För att vara säker på att spelet går lika snabbt på olika snabba datorer bör vi använda deltatiden när vi uppdaterar vår värld.

När vi har satt en maximal uppdateringsfrekvens så spelar deltatiden enbart roll *om* vår uppdatering tar längre tid än mellanrummet mellan två frames. Med 60 fps har vi ca 17ms på oss att uppdatera en frame. En modern dator hinner med förvånansvärt mycket på 17ms.

#### 2. Hantera händelser/events

Allt som händer i omvärlden som påverkar spelet (till exempel knapptryckningar) kallas *händelser* eller *events* och samlas i en kö. (En *kö* i datorvetenskapliga sammanhang fungerar som en kö i verkligheten - det som kommer först in kommer också först ut.)

I varje varv i loopen är det god praxis att *hantera* / *handle* alla händelser / events. Ofta hanterar vi dem genom att strunta i dem. Det händer många fler saker än vad vi bryr oss om, t ex att knappar som inte har någon funktion trycks ned.

Till att börja med hanterar vi bara ```QUIT```-eventet. Det läggs i kön t ex då användaren trycker på ikonen för att stänga fönstret.

Funktionen ```pygame.event.get()``` tar alla objekt som ligger i kön och returnerar dem som en lista som vi går igenom i en ```for```-loop.

```python
    for evt in pygame.event.get():
        if evt.type==pygame.QUIT:
            running = False
```





#### 3. Uppdatera rörelser och spellogik 

