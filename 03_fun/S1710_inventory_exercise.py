"""Opgave "The inventory sequence"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Se de første 3 minutter af denne video:
https://www.youtube.com/watch?v=rBU9E-ZOZAI

Skriv en funktion inventory(), som producerer de tal, der er vist i videoen.
Funktionen accepterer en parameter, der definerer, hvor mange talrækker der skal produceres.
Funktionen udskriver tallene i hver række.

Du vil sandsynligvis ønske at definere en funktion count_number(), som tæller, hvor ofte
et bestemt antal optræder i den aktuelle talrække.

I hovedprogrammet kalder du inventory() med fx 6 som argument.

Hvis du ikke har nogen idé om, hvordan du skal begynde, kan du kigge på løsningen
i S1720_inventory_solution.py

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


def inventory(num_rows):
    numbers = []
    currrow = []

    for row in range(num_rows):
        currrow = []
        for n in range(9999):
            count = count_number(numbers, n)
            if n <= len(numbers):
                numbers.append(count)
                currrow.append(count)
            if count == 0:
                break

        #print
        for num in currrow:
            print(f"{num} ", end='')
        print()


def count_number(numbers, num):
    count = 0
    for n in numbers:
        if n == num:
            #print(f"counted {num} with {n}")
            count += 1
    return count


inventory(16)
