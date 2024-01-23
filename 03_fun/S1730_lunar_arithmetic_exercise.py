"""Opgave "Lunar arithmetic"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Se de første 3 minutter af denne video:
    https://www.youtube.com/watch?v=cZkGeR9CWbk

Del 2:
    Skriv en klasse Lunar_int(), med metoder, der gør, at du kan anvende operatorerne + og * på
    objekter af denne klasse, og at resultaterne svarer til de regler, der forklares i videoen.

Del 3:
    Se resten af videoen.

Del 4:
    Skriv en funktion calc_lunar_primes(n), som retunerer en liste med de første n lunar primes.


Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


class Lunar_int:
    value = 0

    def __init__(self, _value):
        self.value = _value

    def __set__(self, instance, value):
        instance.value = value

    def __add__(self, other):
        result = 0

        v = self.value
        o = other

        i = 1
        while v > 0:
            result += max(v % 10, o % 10) * i
            v //= 10
            o //= 10
            i *= 10

        return Lunar_int(result + o * i)

    def __mul__(self, other):
        result = Lunar_int(0)
        subresults = []

        v = self.value
        o = other

        i = 1
        j = 1
        while v > 0:
            while o > 0:
                r = min((v % 10), (o % 10)) * (i * j)
                subresults.append(r)

                o //= 10
                j *= 10

            o = other
            j = 1

            v //= 10
            i *= 10

        for sr in subresults:
            result += sr

        return result

    def __repr__(self):
        return f"{self.value}"


li = Lunar_int(66)

print(li * 55)
