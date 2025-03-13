## Grundstruktur

### **Uppgift: Skapa ett tomt spelskal**
Skriv ett grundläggande Pygame-spel genom att implementera varje del i följande ordning.

---

#### **Del 1: Grundläggande boilerplate**
- Importera Pygame.
- Skapa konstanter för skärmstorlek.

---

#### **Del 2: Initialisera Pygame**
- Skapa en huvudfunktion för spelet
- Skriv kod som:
  - Initierar Pygame.
  - Skapar en skärm med angiven storlek.
  - Skapar en klocka för att styra uppdateringsfrekvensen.
  - Returnerar skärmen och klockan.

---

#### **Del 3: Skapa huvudloopen**
- Lägg till en spelloop som:
  - Använder klockan för att styra uppdateringsfrekvensen
  - Hanterar händelser
  - Rensar skärmen och ritar om allt.
  - Uppdaterar skärmen

---

#### **Del 4: Anropa huvudfunktionen**
- Lägg till kod som anropar huvudfunktionen
- Använd `if __name__ == "__main__"` för att följa pythonstandard.

---

#### **Del 5: Skapa `Player`-klassen**
- Lägg till en klass spelare med:
  - En konstruktor som tar in och sparar startposition.
  - En uppdateringsmetod som hanterar spelarens rörelse (men inte gör något än)
  - En rita-metod som ritar ut spelaren (men inte gör något än)

---

#### **Del 6: Implementera uppdateringsfunktionen i spelarklassen**
- I uppdateringsfunktionen lägg till kod som:
  - Hämtar tangentbordsinmatning.
  - Flyttar spelaren i rätt riktning.
  - Uppdaterar spelarens position

---

#### **Del 7: Implementera rita-metoden i `Player`**
- I rita-metoden, lägg till kod som:
  - Ritar spelaren på skärmen som en rektangel.

---

#### **Del 8: Lägg till spelaren i spelet**
- Instansiera ett spelarobjekt i huvudfunktionen.
- Anropa uppdateringsfunktionen och rita-funktion i varje varv av spelloopen.

---

#### **Del 9: Skapa en godisklass**
- Lägg till en godisklass `Candy` med:
  - En konstruktor som placerar godisen slumpmässigt.
  - En uppdateringsmetod (som gör vaddå?)
  - En rita-metod

---

#### **Del 10: Lägg till godisar i spelet**
- Skapa och lagra ett antal godisobjekt.
- Uppdatera och rita varje godis för varje varv i speloopen
    - Anropa uppdateringsfunktionen och rita-funktion i varje varv av spelloopen.

---

#### **Del 11: Lägg till hitboxar
- I både godisklassen och spelarklassen:
    - Lägg till en metod `get_rect()` eller ett attribut `rect` som innehåller objektets hitbox.

--- 

#### **Del 11: Lägg till kommentarer i huvudloopen

- Lägg till kommentarer i huvudloopen som beskriver var:
  - Kollisioner kontrolleras
  - Objekt städas upp

---

#### **Möjlig fortsättning**
- Implementera kollision mellan spelaren och godisar
- Lägg till grundstrukturen för en fiende

