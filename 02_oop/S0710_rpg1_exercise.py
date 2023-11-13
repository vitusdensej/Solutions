"""Opgave: Objektorienteret rollespil, del 1 :

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Definer en klasse "Character" med attributterne "name", "max_health", "_current_health", "attackpower".
_current_health skal være en protected attribut, det er ikke meningen at den skal kunne ændres udefra i klassen.

Tilføj en konstruktor (__init__), der accepterer klassens attributter som parametre.
Tilføj en metode til udskrivning af klasseobjekter (__repr__).

Tilføj en metode "hit", som reducerer _current_health af en anden karakter med attackpower.
Eksempel: _current_health=80 og attackpower=10: et hit reducerer _current_health til 70.

Metoden hit må ikke ændre den private attribut _current_health i en (potentielt) fremmed klasse.
Derfor definerer vi en anden metode get_hit, som reducerer _current_health for det objekt, som den tilhører, med attackpower.

Tilføj en klasse "Healer", som arver fra klassen Character.
En healer har attackpower=0 men den har en ekstra attribut "healpower".

Tilføj en metode "heal" til "Healer", som fungerer som "hit" men forbedrer sundheden med healpower.
For at undgå at "heal" forandrer den protected attribut "_current_health" direkte,
tilføj en metode get_healed til klassen Character, som fungerer lige som get_hit.

Hvis du er gået i stå, kan du spørge google, de andre elever eller læreren (i denne rækkefølge).
Hvis du ikke aner, hvordan du skal begynde, kan du åbne S0720_rpg1_help.py og starte derfra.

Når dit program er færdigt, skal du skubbe det til dit github-repository
og sammenlign det med lærerens løsning i S0730_rpg1_solution.py

Send derefter denne Teams-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

class Character:
    name = ""
    max_health = 100
    _current_health = max_health
    attackpower = 10

    def __init__(self, n, mh, ch, ap):
        self.name = n
        self.max_health = mh
        self._current_health = ch
        self.attackpower = ap

    def __repr__(self):
        return f"name: {self.name}, hp: {self._current_health}/{self.max_health}, atk: {self.attackpower}";

    def hit(self, character):
        character.get_hit(self.attackpower)

    def get_hit(self, atkpower):
        self._current_health -= atkpower

    def get_heal(self, healpower):
        self._current_health += healpower

class Healer(Character):
    healpower = 10

    def __init__(self, n, mh, ch, hp):
        super().__init__(n, mh, ch, 0)
        self.healpower = hp

    def __repr__(self):
        return super().__repr__() + ", healpower: " + str(self.healpower)

    def heal(self, character):
        character.get_heal(self.healpower)


chr1 = Character("John", 100, 100, 10)
chr2 = Character("Evil Lord of Darkness", 20000, 50, 1)
chr3 = Healer("Nurse", 20000, 50, 20)

print(chr1)
print(chr2)
print(chr3)
print()
chr1.hit(chr2)
print(chr1)
print(chr2)
print(chr3)
print()
chr3.heal(chr2)
print(chr1)
print(chr2)
print(chr3)
