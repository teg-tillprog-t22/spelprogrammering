## Grundstruktur

### **Uppgift: Skapa ett tomt spelskal**
Skriv ett grundläggande Pygame-spel genom att implementera varje del i följande ordning.

---

#### **Del 1: Grundläggande boilerplate**
- Importera Pygame.
- Skapa konstanter för skärmstorlek.

---

#### **Del 2: Initialisera Pygame**
- Skapa en funktion `init_game()` som:
  - Initierar Pygame.
  - Skapar en skärm med angiven storlek.
  - Skapar en klocka för att styra uppdateringsfrekvensen.
  - Returnerar skärmen och klockan.

---

#### **Del 3: Skapa huvudloopen**
- Skapa en hvuudfunktion som:
  - Innehåller en spelloop.
  - Använder klockan för att styra uppdateringsfrekvensen
  - Hanterar händelser
  - Rensar skärmen och ritar om allt.
  - Uppdaterar skärmen

---

### **Del 4: Anropa huvudfunktionen**
- Lägg till kod som anropar huvudfunktionen
- Använd `if __name__ == "__main__"` för att följa pythonstandard.

---

### **Del 5: Skapa `Player`-klassen**
- Lägg till en klass spelare med:
  - En konstruktor som tar in och sparar startposition.
  - En uppdateringsmetod som hanterar spelarens rörelse (men inte gör något än
  - En rita-metod som ritar ut spelaren (men inte gör något än)

---

### **Del 6: Implementera uppdateringsfunktionen i spelarklassen
- I uppdateringsfunktionen lägg till kod som:
  - Hämtar tangentbordsinmatning.
  - Flyttar spelaren i rätt riktning.
  - Uppdaterar spelarens position

---

### **Del 7: Implementera rita-metoden i `Player`**
- I rita-metoden, lägg till kod som:
  - Ritar spelaren på skärmen som en rektangel.

---

To be continued 
