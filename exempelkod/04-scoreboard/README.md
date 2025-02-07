## TillProg Spelprogrammering VT25
[⬅️ Gå tillbaka till startsidan](../../README.md)

### Enkel scoreboard-hantering med text

I det här exemplet lägger vi till en **poängräkning** (scoreboard) i spelet, så att spelaren kan se hur många poäng hen har samlat ihop genom att äta godisar. För att göra detta använder vi Pygames **font-modul** och renderar text direkt på skärmen.

---

### 1. Font och text

Innan spelet startar, initialiserar vi Pygames font-modul och väljer en standardfont:

```python
pygame.font.init()
font = pygame.font.Font(None, 36) 
```

- `pygame.font.init()` ser till att font-hanteringen är redo att användas.  
- `pygame.font.Font(None, 36)` skapar ett “font-objekt” med en viss textstorlek (36 px). `None` anger en standardfont.

---

### 2. Rita ut poängen (scoreboard)

Under rit-fasen i huvudloopen skapar vi en textsträng och renderar den till en “text-surface”. En rityta som är lika stor som och bara innehåller själva texten.

```python
text = f"Score: {player.points}"
text_surface = font.render(text, True, "white")
screen.blit(text_surface, (10, 10))
```

1. **Sträng**: Vi bygger `text` genom att använda spelarens attribut `player.points` i en f-sträng.
2. **Rendera** (rita) text: Med `font.render(text, True, "white")` skapar vi en *Surface* (rityta/bild) med vit text på genomskinlig bakgrund.
3. **Blit** (kopiera) ytan till skärmen: `screen.blit(text_surface, (10, 10))` kopierar (ritar) textens pixlar till skärmens *Surface*. Metoden *blit* är ett kort namn för *block image transfer*, dvs. en överföring av en rektangulär bild från en yta till en annan.

> *Rendera* och *rita* betyder alltså i praktiken samma sak i detta sammanhang: vi gör en bild av texten och lägger sedan ut den på skärmen. Här använder vi en fast position (10, 10) på skärmen, men det är lätt att ändra till någon annanstans eller kanske med text som rör sig (svårare).

---

### Sammanfattning

- **Font-initialisering** måste göras innan du kan rita text.  
- **Rendera text** genom att skapa en bild av texten och sedan “blitta” den på skärmen.  
- Poängräkningen kopplas direkt till spelarens attribut `points`, så varje gång en godis äts upp ökar poängen.

Denna metod är såklart enkel att utöka med mer information, t ex antal liv kvar, tid, FPS osv.
