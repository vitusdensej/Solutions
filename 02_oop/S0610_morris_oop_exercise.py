"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Omskriv din oprindelige Morris-kode til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


class Morris:
    def __init__(self):
        pass

    sleepiness = 0
    hunger = 0
    whisky = 0
    thirst = 0
    gold = 0

    def sleep(self):
        self.sleepiness -= 10
        self.thirst += 1
        self.hunger += 1

    def mine(self):
        self.sleepiness += 5
        self.thirst += 5
        self.hunger += 5
        self.gold += 5

    def eat(self):
        self.sleepiness += 5
        self.thirst -= 5
        self.hunger -= 20
        self.gold -= 2

    def buy_whisky(self):
        self.sleepiness += 5
        self.thirst += 1
        self.hunger += 1
        self.whisky += 1
        self.gold -= 1

    def drink(self):
        self.sleepiness += 5
        self.thirst -= 15
        self.hunger -= 1
        self.whisky -= 1

    def check_dead(self):
        return self.sleepiness > 100 or self.hunger > 100 or self.thirst > 100


def loop():
    morris = Morris()

    for turn in range(1000):
        if(morris.check_dead()):
            print(f"ended with {morris.gold} gold, {morris.thirst} thirst, {morris.hunger} hunger, {morris.whisky} whisky, "
                  f"{morris.sleepiness} sleep, {turn + 1} turn")
            return False

        if morris.thirst + 5 > 100:
            morris.drink()
        elif morris.hunger + 5 > 100:
            morris.eat()
        elif morris.sleepiness + 15 > 100:
            morris.sleep()
        elif morris.whisky <= 0 and morris.gold >= 1:
            morris.buy_whisky()
        else:
            morris.mine()

    print(f"ended with {morris.gold} gold, {morris.thirst} thirst, {morris.hunger} hunger, {morris.whisky} whisky, "
          f"{morris.sleepiness} sleep, {turn + 1} turn")
    return True


if not loop():
    print("but ded :(")