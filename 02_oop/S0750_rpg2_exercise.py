"""opgave: Objektorienteret rollespil, del 2 :

Som altid skal du læse hele øvelsesbeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Byg videre på din løsning af del 1.

Opfind to nye klasser, som arver fra klassen Character. For eksempel Hunter og Magician.
Dine nye klasser skal have deres egne ekstra metoder og/eller attributter.
Måske overskriver de også metoder eller attributter fra klassen Character.

Lad i hovedprogrammet objekter af dine nye klasser (dvs. rollespilfigurer) kæmpe mod hinanden,
indtil den ene figur er død. Udskriv, hvad der sker under kampen.

I hver omgang bruger en figur en af sine evner (metoder). Derefter er det den anden figurs tur.
Det er op til dig, hvordan dit program i hver tur beslutter, hvilken evne der skal bruges.
Beslutningen kan f.eks. være baseret på tilfældighed eller på en smart strategi

Opgradering 1:
Hver gang en figur bruger en af sine evner, skal du tilføje noget tilfældighed til den anvendte evne.

Opgradering 2:
Lad dine figurer kæmpe mod hinanden 100 gange.
Hold styr på resultaterne.
Prøv at afbalancere dine figurers evner på en sådan måde, at hver figur vinder ca. halvdelen af kampene.

Hvis du går i stå, kan du spørge google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-besked til din lærer: <filename> done
Fortsæt derefter med den næste fil."""

import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


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
        if self._current_health + healpower > self.max_health:
            self._current_health = self.max_health
        else:
            self._current_health += healpower

    def use_strat(self, myteam, otherteam):
        targetindex = random.randint(0, len(otherteam) - 1)
        self.hit(otherteam[targetindex])
        return ["hit", otherteam[targetindex].name]

    def get_target(self, myteam, otherteam, targetfriendly):
        pass

class Healer(Character):
    healpower = 10

    def __init__(self, n, mh, ch, hp):
        super().__init__(n, mh, ch, 0)
        self.healpower = hp

    def __repr__(self):
        return super().__repr__() + ", healpower: " + str(self.healpower)

    def heal(self, character):
        character.get_heal(self.healpower)

    def use_strat(self, myteam, otherteam):
        #random.randint(1)
        targetindex = random.randint(0, len(myteam) - 1)
        self.heal(myteam[targetindex])
        return ["heal", myteam[targetindex].name]

class BillGates(Character):
    totalmoney = 1000000

    def __init__(self, n, mh, ch, ap, tm):
        super().__init__(n, mh, ch, ap)
        self.totalmoney = tm

    def __repr__(self):
        return super().__repr__() + f", money: {self.totalmoney}"

    def throw_money(self, character):
        amount = random.randint(10, int(self.totalmoney / 40))
        self.totalmoney -= amount
        character.get_hit(amount)

    def heal_money(self, character):
        amount = random.randint(10, int(self.totalmoney / 40))
        self.totalmoney -= amount
        character.get_heal(amount)

    def use_strat(self, myteam, otherteam):
        if self.totalmoney <= 0:
            return super().use_strat(myteam, otherteam)

        action = random.randint(0, 1)

        if action == 0:
            targetindex = random.randint(0, len(myteam) - 1)
            self.heal_money(myteam[targetindex])
            return ["threw healing money", [otherteam[targetindex].name]]
        else:
            targetindex = random.randint(0, len(otherteam) - 1)
            self.throw_money(otherteam[targetindex])
            return ["threw money", [otherteam[targetindex].name]]


class Uno(Character):
    def giveplus4(self, character):
        self.attackpower += 4
        self.hit(character)

    def use_strat(self, myteam, otherteam):
        action = random.randint(0, 1)

        if action == 0:
            return super().use_strat(myteam, otherteam)
        else:
            targetindex = random.randint(0, len(otherteam) - 1)
            self.giveplus4(otherteam[targetindex])
            return ["gave +4", otherteam[targetindex].name]

team1 = [Character("John", 100, 100, 10),
        Character("Evil Lord of Darkness", 20000, 2000, 1),
        Healer("Nurse", 20000, 50, 20)]

team2 = [Character("Evil John of Destruction", 100, 100, 10),
        BillGates("Bill Gates", 1000, 50, 1, 99999),
        Uno("Spillet Uno", 1000, 50, 20)]

def get_turn_chr(t):
    global team1
    global team2

    if t < 3:
        return team1[t]
    else:
        return team2[t - 3]

# det her er lidt dumt aaaaaaaa
def get_myteam(t):
    global team1
    global team2

    if t < 3:
        return team1
    else:
        return team2

def get_otherteam(t):
    global team1
    global team2

    if t < 3:
        return team2
    else:
        return team1

turn = 0
def do_turn():
    global turn
    global team1
    global team2

    chr = get_turn_chr(turn % 6)

    if chr._current_health > 0:
        msg = chr.use_strat(get_myteam(turn % 6), get_otherteam(turn % 6))
        print(f"{chr.name} used {msg[0]} on {msg[1]}!")

    if turn % 6 == 0:
        print()
        print(f"end of round! stats:")
        for t1 in team1:
            #print(f"{bcolors.OKGREEN} {t1}")
            print(t1)
        print("---------")
        for t2 in team2:
            #print(f"{bcolors.FAIL} {t2}")
            print(t2)
        print(f"next round!")
        print()
        #print("bcolors.HEADER")

    turn += 1

def team_alive():
    currstatus = 0

    for t in team1:
        # hehe
        if t._current_health > 0:
            currstatus = 0
            break
        else:
            currstatus = 1

    if currstatus != 0:
        return currstatus

    for t2 in team2:
        # hehe
        if t2._current_health > 0:
            currstatus = 0
            break
        else:
            currstatus = 2

    return currstatus

while team_alive() == 0:
    do_turn()

if team_alive() == 1:
    print("team2 wins!")
else:
    print("team1 wins!")


