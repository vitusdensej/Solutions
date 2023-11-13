"""
Opgave "Animals"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Alt, hvad du har brug for at vide for at løse denne opgave, finder du i cars_oop-filerne.

Definer en klasse ved navn Animal.
Hvert objekt i denne klasse skal have attributterne name (str), sound (str), height (float),
weight (float), legs (int), female (bool).
I parentes står data typerne, dette attributterne typisk har.

Tilføj til klassen meningsfulde metoder __init__ og __repr__.
Kald disse metoder for at oprette objekter af klassen Animal og for at udskrive dem i hovedprogrammet.

Skriv en klassemetode ved navn make_noise, som udskriver dyrets lyd i konsollen.
Kald denne metode i hovedprogrammet.

Definer en anden klasse Dog, som arver fra Animal.
Hvert objekt af denne klasse skal have attributterne tail_length (int eller float)
og hunts_sheep (typisk bool).

Tilføj til klassen meningsfulde metoder __init__ og __repr__.
Ved skrivning af konstruktoren for Dog skal du forsøge at genbruge kode fra klassen Animal.
Kald disse metoder for at oprette objekter af klassen Hund og for at udskrive dem i hovedprogrammet.

Kald metoden make_noise på Dog-objekter i hovedprogrammet.

Skriv en klassemetode ved navn wag_tail for Dog.
Denne metode udskriver i konsollen noget i stil med
"Hunden Snoopy vifter med sin 32 cm lange hale"
Kald denne metode i hovedprogrammet.

Skriv en funktion mate(mother, father). Begge parametre er af typen Dog.
Denne funktion skal returnere et nyt objekt af typen Dog.
I denne funktion skal du lave meningsfulde regler for den nye hunds attributter.
Hvis du har lyst, brug random numbers så mate() producerer tilfældige hunde.
Sørg for, at denne funktion kun accepterer hunde med det korrekte køn som argumenter.

I hovedprogrammet kalder du denne metode og udskriver den nye hund.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


class Animal:
    name = ""
    sound = ""
    height = 0.0
    weight = 0.0
    legs = 0
    female = False

    def __init__(self, name_, sound_, height_, weight_, legs_, female_):
        self.name = name_
        self.sound = sound_
        self.height = height_
        self.weight = weight_
        self.legs = legs_
        self.female = female_

    def __repr__(self):
        return f"{self.name} {self.sound}, {self.height}, {self.weight}, {self.legs}, {self.female}"

    def make_noise(self):
        print(f"{self.sound}")


class Dog(Animal):
    tail_length = 0.0
    hunts_sheep = True

    def __init__(self, name_, sound_, height_, weight_, legs_, female_, taillen_, huntsheep_):
        super().__init__(name_, sound_, height_, weight_, legs_, female_)
        self.tail_length = taillen_
        self.hunts_sheep = huntsheep_

    def __repr__(self):
        return super().__repr__() + f", {self.tail_length}, {self.hunts_sheep}"

    def wag_tail(self):
        extra = self.female is True if "hun" else "han"
        extra2 = self.hunts_sheep is False if "i mens den jager får" else ""
        print(f"Hunden {self.name} som er {self.height} høj og {self.weight} bred og er {(extra)} og har {self.legs} mændge af ben, vifter med dens {self.tail_length} m lange hale {extra2}")


def mate(mother, father):
    if mother.female == father.female:
        return False

    return Dog(mother.name + father.name, mother.sound + father.sound, (mother.height + father.height) / 2,
               (mother.weight + father.weight) / 2, (mother.legs + father.legs) / 2, True, (mother.tail_length + father.tail_length) / 2,
               True)


dog = Dog("sej hund", "roar", 180, 9, 5, False, 5, True)
dog2 = Dog("sej hund number 2", "roar haha", 199, 10, 5, True, 5, True)

dog.wag_tail()
dog2.wag_tail()

dog3 = mate(dog, dog2)
print(dog3)