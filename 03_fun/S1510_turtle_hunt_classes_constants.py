"""Opgave "Turtle Hunt":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Spillet:
    Denne øvelse er et spil for 2 spillere.
    3 skildpadder (jægere) forsøger at fange en anden skildpadde (bytte) så hurtigt som muligt.
    Den ene spiller styrer byttet, den anden spiller styrer jægerne. Derefter bytter spillerne roller.
    I hver tur bestemmer spillerne, hvor mange grader deres skildpadde(r) roterer. Dette er spillerens eneste opgave.
    Byttet får et point for hver tur, før det bliver fanget.
    Hvis byttet stadig er på flugt efter MAX_TURNS omgange, fordobles pointene, og jagten slutter.


Koden til spillet er allerede skrevet i S1530_turtle_hunt_main.py og S1520_turtle_hunt_service.py. Du må ikke ændre disse filer.

Din opgave er at få skildpadderne til at rotere smartere.

Kopier alle 3 turtle_hunt-filer til din egen løsningsmappe.
Skriv din løsning ind i din kopi af S1510_turtle_hunt_classes_constants.py.

Filstruktur:
    Koden er opdelt i 3 filer for at gøre det klart, hvilken del af koden
    du skal ændre, og hvilken del af koden du skal lade være uændret.

    S1530_turtle_hunt_main.py:
        Dette er hovedprogrammet.
        Du må ikke foretage ændringer heri.
        Kør det for at starte spillet.

    S1520_turtle_hunt_service.py:
        Indeholder nogle servicefunktioner, som vil være nyttige for dig.
        Du må ikke foretage ændringer heri.

    Denne fil (S1510_turtle_hunt_classes_constants.py):
        Alt din programmering til denne øvelse foregår i denne fil.

Delopgaver:
Trin 1:
    Kig på programkoden.
    Du behøver ikke at forstå alle detaljer i hovedprogrammet.
    Forstå, hvordan de tre filer importerer hinandens kode med "import".
    Forstå, hvornår og hvordan metoderne rotate_prey() og rotate_hunt() bruges.
    Fra nu af foregår al din programmering til denne øvelse i denne fil her.

Trin 2:
    Ændr navnet på klassen PlayerName1 i den første linje i dens klassedefinition til dit personlige klasses navn.
    Nederst i denne fil skal du sætte variablerne class1 og class2 til dit personlige klasses navn.

Trin 3:
    I din personlige klasse skal du gøre metoderne rotate_prey og rotate_hunter smartere.
    Eventuelt vil du også tilføje nogle attributter og/eller metoder til din klasse.
    Du må dog ikke manipulere (f.eks. flytte) skildpadderne med din kode.
    Køretiden for dine metoder rotate_prey og rotate_hunter skal være mindre end 0,1 sekunder pr. iteration.

Trin 4:
    Find en sparringspartner i din studiegruppe.
    Som med alt andet skal du bede din lærer om hjælp, hvis det er nødvendigt.
    I din kode skal du erstatte hele klassen PlayerName2 med din sparringspartners klasse.
    Nederst i denne fil indstiller du variablen class2 til din sparringpartners klasses navn.
    Lad de 2 klasser kæmpe og lær af resultaterne for at forbedre din kode.
    Gentag dette trin indtil du er tilfreds :-)

Trin 5:
    Når dit program er færdigt, skal du skubbe det til dit github-repository.
    Send derefter denne Teams-besked til din lærer: <filename> done
    Derefter fortsætter du med den næste fil.

Senere:
    Når alle er færdige med denne øvelse, afholder vi en turnering
    for at finde ud af, hvem der har programmeret de klogeste skildpadder :)

Kun hvis du er nysgerrig og elsker detaljer:
    Her er den fulde dokumentation for skildpaddegrafikken:
    https://docs.python.org/3.3/library/turtle.html"""

import math
import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.
import random
from S1520_turtle_hunt_service import distance, direction

MAX_POS = 300

def normalize(vec):
    length = math.sqrt(vec[0] * vec[0] + vec[1] * vec[1])
    return [vec[0] / length, vec[1] / length]


class PreyHunterInfo:
    index = -1
    last_position = [0,0]
    orientation = [0,0]
    distance_toprey = 0


class Bob(turtle.Turtle):

    prey_orientation = 0
    prey_last_position = [0, 0]
    prey_orientation_vector = []

    preyhunter_info = [PreyHunterInfo(), PreyHunterInfo(), PreyHunterInfo()]

    def __init__(self):
        super().__init__()  # Here, this is equivalent to turtle.Turtle.__init__(self)
        self.orientation = 0  # used to keep track of the turtle's current orientation (the direction it is heading)

    def find_hunter_closets(self, positions):
        closest = -1
        currdist = 10000
        for i in range(1, len(positions)):
            dist = distance(positions[0], positions[i])
            if dist < currdist:
                closest = i
                currdist = dist
        return closest

    def get_hunter_dists(self, positions):
        dists = []
        for i in range(1, len(positions)):
            dists.append(distance(positions[0], positions[i]))
        return dists

    def get_hunter_index(self, positions):
        for p in range(1, len(positions)):
            if distance(positions[p], self.pos()) < 0.1:
                return p

    def get_hunter_dist_order(self, dists):
        dlist = {}
        for d in range(len(dists)):
            dlist[d] = dists[d]
        #print(dict(sorted(dlist.items(), key=lambda x:x[1], reverse=True)))
        return dict(sorted(dlist.items(), key=lambda x:x[1], reverse=False))

    def get_hunter_mydistorder(self, myindex, dists):
        dict = self.get_hunter_dist_order(dists)
        for d in range(len(dict.keys())):
            if tuple(dict.keys())[d] == myindex - 1:
                return d;
        return -1

    def angle_to_vec(self):
        radians = math.radians(self.orientation)
        return [math.cos(radians), math.sin(radians)]

    def bounce_vec_off_wall(self, start, vec, wall_location, wall_axis):
        disttowall = distance(start, wall_location)
        newvec = [vec[0], vec[1]]
        # idk if this is correct math wise
        #newvec[0] -= disttowall
        #newvec[1] -= disttowall
        if wall_axis == 0: # up down
            newvec[0] *= -1
        else: # right left
            newvec[1] *= -1
        return wall_location # todo make this function work lol
        return [newvec[0] + start[0], newvec[1] + start[1]]


    def rotate_prey(self, positions):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        # self: the turtle that shall be rotated
        # positions: a list of tuples. Each tuple is a pair of coordinates (x,y).
        # positions[0] is the coordinate tuple of the prey. positions[0][0] is the x-coordinate of the prey.
        # positions[1], positions[2], positions[3] refer to the hunters.
        # for example is positions[3][1] the y-coordinate of the third hunter.

        # Example for use of the service functions distance() and direction
        # print(f'{distance(positions[0], positions[1])=}   {direction(positions[0], positions[1])=}')  # print distance and direction from prey to hunter1

        for i in range(1, len(positions)):
            x = self.preyhunter_info[i - 1].last_position[0] - positions[i][0]
            y = self.preyhunter_info[i - 1].last_position[1] - positions[i][1]
            self.preyhunter_info[i - 1].orientation = normalize([x, y])
            self.preyhunter_info[i - 1].last_position = positions[i]
            self.preyhunter_info[i - 1].dist_toprey = distance(positions[0], positions[i])
            self.preyhunter_info[i - 1].index = i - 1

        degree = 0
        currscaredof = self.find_hunter_closets(positions)

        hdir = direction(self.position(), positions[currscaredof])
        degree = hdir + 180
        degree -= self.orientation

        # steer away from wall
        """nextpos = [self.pos()[0] + self.angle_to_vec()[0] * STEP_SIZE,
                   self.pos()[1] + self.angle_to_vec()[1] * STEP_SIZE]
        if nextpos[0] > MAX_POS - 30:
            bounce = nextpos
            bounce[0] = self.position()[0]
            degree = direction(self.pos(), bounce) - self.orientation"""

        self.orientation += degree
        self.orientation %= 360
        # print(self.orientation)
        return degree

    def rotate_hunter(self, positions):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        # Example for use of the service functions distance() and direction
        # print(f'{distance(self.position(), positions[0])=}   {direction(self.position(), positions[0])=}')  # print distance and direction from the current hunter to the prey

        self.prey_orientation = direction(self.prey_last_position, positions[0])
        self.prey_orientation_vector = positions[0] - self.prey_last_position # this isn't normalized (:
        self.prey_last_position = positions[0]

        degree = 0

        #closests = self.find_hunter_closets(positions)
        hunter_dists = self.get_hunter_dists(positions)
        myindex = self.get_hunter_index(positions)
        mydistorder = self.get_hunter_mydistorder(myindex, hunter_dists)

        #print(mydistorder)

        if mydistorder == 0:
            degree = self.hunter_directchase(positions)
        elif mydistorder == 1:
            # should prop use the pythagorean theorem here, but i'll do it later
            # or maybe not idk
            degree = self.hunter_chaseahead(positions)
        else:
            degree = self.hunter_chasebehind(positions)

        self.orientation += degree
        self.orientation %= 360
        # print(self.orientation)
        return degree

    def hunter_directchase(self, positions):
        return direction(self.position(), positions[0]) - self.orientation

    def hunter_chaseahead(self, positions):
        prey_future_pos = positions[0] + self.prey_orientation_vector * distance(self.position(), positions[0])
        prey_future_pos_true = self.bounce_vec_off_wall(positions[0], prey_future_pos, [MAX_POS, 0], 0)

        return direction(self.position(), prey_future_pos_true) - self.orientation

    def hunter_chasebehind(self, positions):
        return direction(self.pos(), positions[0] + self.prey_orientation_vector * -25) - self.orientation


#  Insert the code of your sparring partner's turtle class here:
#
#
#
#


# change these global constants only for debugging purposes:
#MAX_TURNS = 100       # Maximum number of turns in a hunt.                           In competition: probably 200.
MAX_TURNS = 200       # Maximum number of turns in a hunt.                           In competition: probably 200.
ROUNDS = 1            # Each player plays the prey this often.                       In competition: probably 10.
STEP_SIZE = 3         # Distance each turtle moves in one turn.                      In competition: probably 3.
SPEED = 0             # Fastest: 10, slowest: 1, max speed: 0.                       In competition: probably 0.
CAUGHT_DISTANCE = 10  # Hunt is over, when a hunter is nearer to the prey than that. In competition: probably 10.


random.seed(2)  # use seed() if you want reproducible random numbers for debugging purposes. You may change the argument of seed().


class1 = Bob  # (red prey) Replace Bob by your own class name here.
class2 = Bob  # (green prey) For testing your code, replace Bob by your own class name here. Later replace this by your sparring partner's class name.
