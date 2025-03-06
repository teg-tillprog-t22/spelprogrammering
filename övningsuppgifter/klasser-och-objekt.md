### Uppgift 1: Vad är en klass?
1.) Förklara skillnaden mellan en **klass** och en **instans (objekt)**.

---

#### Lösning:
- En **klass** är en _mall_ för att skapa objekt.
- En **instans** är ett enskilt objekt som skapats från en klass.

---

### Uppgift 2: Vad gör `__init__()`?
2.) Vad gör metoden `__init__()` i en klass? Varför kallas den en **konstruktor**?

---

#### Lösning:
- `__init__()` körs automatiskt vid skapandet av en ny instans och används för att definiera objektets starttillstånd.
- Den kallas **konstruktor** eftersom den "konstruerar" eller skapar objektet.

---

### Uppgift 3: Vad gör `self`?
3.) Vad är syftet med `self` i en metod i en klass?

---

#### Lösning:
- `self` refererar till _instansen_ av klassen och används för att komma åt objektets **attribut** och **metoder**.

---

### Uppgift 4: Vad är ett attribut?
4.) Vad är ett **attribut** i en klass? Hur skiljer den sig från en vanlig variabel och en global variabel?

---

#### Lösning:
- Ett **attribut** är en variabel som är kopplad till en instans och lagrar objektets tillstånd. Varje instans har sin egen uppsättning av attribut.
- En vanlig variabel är lokal och finns bara inom en funktion eller metod. Om variabeln är definierad utanför alla funktioner är den global och kan användas överallt.

---

### Uppgift 5: Vad händer här?
5.) Vad skrivs ut av följande kod?

```python
class Dog:
    def __init__(self, name):
        self.name = name

dog1 = Dog("Bianca")
dog2 = Dog("Selma")

print(dog1.name)
print(dog2.name)
```

---

#### Lösning:
```
Bianca
Selma
```
Varje instans får sitt eget attribut `name`.

---

### Uppgift 6: Vad gör en metod?
6.) Vad är en **metod** i en klass? Hur skiljer den sig från en vanlig funktion?

---

#### Lösning:
- En **metod** är en funktion som _tillhör_ en klass och anropas för en viss _instans_.
- Den skiljer sig från en vanlig funktion genom att den är definierad inuti i en klass och alltid har `self` som första argument.

---

### Uppgift 7: Vad skrivs ut?
7.) Vad skrivs ut av följande kod?

```python
class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

c = Counter()
c.add()
c.add()
print(c.count)
```

---

#### Lösning:
```
2
```

### Uppgift 8: Lista som attribut
8.) Skapa en klass `Notebook` där varje instans har en lista `notes`. Lägg till en metod `add_note(note)` som lägger till en anteckning i listan.

---

#### Lösning:

```python
class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)
```

---

### Uppgift 9: Förstå `self`
9.) Vad händer om vi tar bort `self` från metoden `add_note`nedan? Vad blir felet?

```python
class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)
```


---

#### Lösning:
- Utan `self` kan vi inte komma åt objektets attribut och metoder.
- Vi får ett **NameError** eftersom Python inte vet vad `self.notes` är.

---

### Uppgift 10: Förklara denna kod
10.) Vad gör denna kod?

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alex", 30)
p.age += 1
print(p.age)
```

---

#### Lösning:
- Skapar en person med `name="Alex"` och `age=30`.
- Ökar åldern med 1.
- Skriver ut `31`.

---

### Uppgift 11: Klassens datatyper
11.) Vilka datatyper används i denna klass?

```python
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

s = Student("Emma", [85, 90, 78])
```

---

#### Lösning:
- `name` är en **sträng** (`str`).
- `grades` är en **lista** (`list` med **heltal** `int`).

---

### Uppgift 12: Vad returneras här?
12.) Vad returneras av `get_name()`?

```python
class User:
    def __init__(self, username):
        self.username = username

    def get_name(self):
        return self.username

u = User("admin")
print(u.get_name())
```

---

#### Lösning:
```
admin
```
- `get_name()` returnerar `self.username`.

---

### Uppgift 13: Objekt i en lista
13.) Vad skrivs ut av denna kod?

```python
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

items = [Item("Apple", 5), Item("Banana", 3)]

for item in items:
    print(item.name)
```

---

#### Lösning:
```
Apple
Banana
```
- `items` är en lista med objekt av typen `Item`, och vi loopar genom dem.

---

### Uppgift 14: Rektangelklass

14a)

Skapa en **klass** `Rectangle` med en **konstruktor** som tar bredd och höjd som **argument**. Lägg till **metoder**:

   - `area()` – Returnerar rektangelns area (bredd * höjd).  
   - `perimeter()` – Returnerar rektangelns omkrets (2 * (bredd + höjd)).

14b) Testa klassen genom att skapa en rektangel och anropa metoderna.

---

#### Lösning:

```python
class Rectangle:
    def __init__(self, width, height):
        """ Skapar en rektangel med angiven bredd och höjd. """
        self.width = width
        self.height = height

    def area(self):
        """ Returnerar rektangelns area. """
        return self.width * self.height

    def perimeter(self):
        """ Returnerar rektangelns omkrets. """
        return 2 * (self.width + self.height)

# Exempelanvändning
r = Rectangle(4, 7)
print(r.area())      # 28
print(r.perimeter()) # 22
```

---

### Uppgift 15: Bankkonto

15a) Skapa en klass `BankAccount` med en *konstruktor* som tar ett startbelopp. Lägg till *metoder*:

   - `deposit(amount)` – Ökar saldot.  
   - `withdraw(amount)` – Minskar saldot om täckning finns.  
   - `balance()` – Returnerar aktuellt saldo.

15b) Testa klassen genom att skapa ett konto, sätta in och ta ut pengar, samt visa aktuellt saldo.

---

#### Lösning:

```python
class BankAccount:
    def __init__(self, initial_balance):
        """ Skapar ett bankkonto med ett startbelopp. """
        self.balance_amount = initial_balance

    def deposit(self, amount):
        """ Sätter in ett belopp på kontot. """
        self.balance_amount += amount

    def withdraw(self, amount):
        """ Tar ut ett belopp om det finns täckning. """
        if amount <= self.balance_amount:
            self.balance_amount -= amount

    def balance(self):
        """ Returnerar aktuellt saldo. """
        return self.balance_amount

# Exempelanvändning
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.balance()) # 1300
```

---

### Uppgift 16: Bilklass

16a) Skapa en klass `Car` med en konstruktor som tar märke och hastighet. Lägg till metoder:

   - `accelerate(speed)` – Ökar hastigheten.  
   - `brake(speed)` – Minskar hastigheten men inte under 0.  
   - `current_speed()` – Returnerar aktuell hastighet.

16b) Testa klassen genom att skapa en bil, öka och bromsa hastigheten samt visa aktuell hastighet.

---

#### Lösning:

```python
class Car:
    def __init__(self, brand, speed):
        """ Skapar en bil med angivet märke och startfart. """
        self.brand = brand
        self.speed = speed

    def accelerate(self, speed):
        """ Ökar bilens hastighet. """
        self.speed += speed

    def brake(self, speed):
        """ Minskar hastigheten, men inte under 0. """
        self.speed = max(0, self.speed - speed)

    def current_speed(self):
        """ Returnerar bilens nuvarande hastighet. """
        return self.speed

# Exempelanvändning
car = Car("Volvo", 50)
car.accelerate(20)
car.brake(30)
print(car.current_speed()) # 40
```

---

### Uppgift 17: Studentklass

18a) Skapa en *klass* `Student` med en *konstruktor* som tar namn. Lägg till *metoder*:

   - `add_grade(subject, grade)` – Sparar betyg per ämne.  
   - `get_grades()` – Returnerar alla betyg.  

Testa klassen genom att skapa en student, lägga till betyg och visa alla betyg.

---

#### Lösning:

```python
class Student:
    def __init__(self, name):
        """ Skapar en student med ett namn och en tom betygslista. """
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        """ Lägger till ett betyg för ett ämne. """
        self.grades[subject] = grade

    def get_grades(self):
        """ Returnerar studentens betyg i alla ämnen. """
        return self.grades

# Exempelanvändning
s = Student("Anna")
s.add_grade("Matematik", "A")
s.add_grade("Historia", "B")
print(s.get_grades()) # {'Matematik': 'A', 'Historia': 'B'}
```
