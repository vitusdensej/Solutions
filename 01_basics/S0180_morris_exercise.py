"""
Opgave "Morris the Miner":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Udgangssituation:
Morris har egenskaberne sleepiness, thirst, hunger, whisky, gold.
Alle attributter har startværdien 0.

Regler:
Hvis sleepiness, thirst eller hunger kommer over 100, dør Morris.
Morris kan ikke opbevare mere end 10 flasker whisky.
Ingen attribut kan gå under 0.

Ved hver omgang kan Morris udføre præcis én af disse aktiviteter:
sleep:      sleepiness-=10, thirst+=1,  hunger+=1,  whisky+=0, gold+=0
mine:       sleepiness+=5,  thirst+=5,  hunger+=5,  whisky+=0, gold+=5
eat:        sleepiness+=5,  thirst-=5,  hunger-=20, whisky+=0, gold-=2
buy_whisky: sleepiness+=5,  thirst+=1,  hunger+=1,  whisky+=1, gold-=1
drink:      sleepiness+=5,  thirst-=15, hunger-=1,  whisky-=1, gold+=0

Din opgave:
Skriv et program, der giver Morris så meget guld som muligt på 1000 omgange.

Hvis du ikke har nogen idé om hvordan du skal begynde, så åbn S0185_morris_help.py og start derfra.
Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

sleepiness = 0
thirst = 0
hunger = 0
whisky = 0
gold = 0

def sleep():
    global sleepiness
    global thirst
    global hunger

    sleepiness -= 10
    thirst += 1
    hunger += 1

def mine():
    global sleepiness
    global thirst
    global hunger
    global gold

    sleepiness += 5
    thirst += 5
    hunger += 5
    gold += 5

def eat():
    global sleepiness
    global thirst
    global hunger
    global gold

    sleepiness += 5
    thirst -= 5
    hunger -= 20
    gold -= 2

def buy_whisky():
    global sleepiness
    global thirst
    global hunger
    global whisky
    global gold

    sleepiness += 5
    thirst += 1
    hunger += 1
    whisky += 1
    gold -= 1

def drink():
    global sleepiness
    global thirst
    global hunger
    global whisky

    sleepiness += 5
    thirst -= 15
    hunger -= 1
    whisky -= 1

def dead_check(thirst, hunger, sleep):
    if thirst > 100 or hunger > 100 or sleep > 100:
        return True
    elif thirst < 0 or hunger < 0 or sleep < 0:
        print("omg u idiot")
    return False

def loop():
    global sleepiness
    global thirst
    global hunger
    global whisky
    global gold

    for turn in range(1000):
        if(dead_check(thirst, hunger, sleepiness)):
            print(f"ended with {gold} gold, {thirst} thirst, {hunger} hunger, {whisky} whisky, {sleepiness} sleep, {turn + 1} turn")
            return False

        if thirst + 5 > 100:
            drink()
        elif hunger + 5 > 100:
            eat()
        elif sleepiness + 15 > 100:
            sleep()
        elif whisky <= 0 and gold >= 1:
            buy_whisky()
        else:
            mine()

    print(f"ended with {gold} gold, {thirst} thirst, {hunger} hunger, {whisky} whisky, {sleepiness} sleep, {turn + 1} turn")
    return True

if not loop():
    print("but ded :(")