""" Opgave "Number guessing"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Opret et program, der spiller et gættespil med brugeren. Programmet fungerer på følgende måde:
    Forklar reglerne for brugeren.
    Generer tilfældigt et 4-cifret heltal.
    Bed brugeren om at gætte et 4-cifret tal.
    Hvert ciffer, som brugeren gætter korrekt i den rigtige position, tæller som en sort mønt.
    Hvert ciffer, som brugeren gætter korrekt, men i den forkerte position, tæller som en hvid mønt.
    Når brugeren har gættet, udskrives det, hvor mange sorte og hvide mønter gættet er værd.
    Lad brugeren gætte, indtil gættet er korrekt.
    Hold styr på antallet af gæt, som brugeren gætter i løbet af spillet, og print det ud til sidst.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
import random

print("Generer tilfældigt et 4-cifret heltal.\
    Bed brugeren om at gætte et 4-cifret tal.\
    Hvert ciffer, som brugeren gætter korrekt i den rigtige position, tæller som en sort mønt.\
    Hvert ciffer, som brugeren gætter korrekt, men i den forkerte position, tæller som en hvid mønt.\
    Når brugeren har gættet, udskrives det, hvor mange sorte og hvide mønter gættet er værd.")

number = str(random.randint(1000, 9999))

numsguesses = 0
blackcoin = 0
whitecoin = 0

#print(f"debug: {number}")

# todo it still counts white coins in annoying situations, but i don't know how to fix that right now

while(True):
    numsguesses += 1
    blackcoin = 0
    whitecoin = 0
    #alreadycountedindex = []
    guess = input("Guess a number ")
    for i in range(len(guess)):
        for j in range(len(number)):
            if guess[i] == number[j]:
                if i == j:
                    blackcoin += 1
                    #alreadycountedindex.append(j)
                #elif j not in alreadycountedindex:
                else:
                    whitecoin += 1
    if blackcoin == 4:
        break
    else:
        print(f"Black Coins: {blackcoin}, White Coins {whitecoin}")

print(f"You Guessed it in {numsguesses} guesses!")

