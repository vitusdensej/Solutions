"""
Opgave "Tom the Turtle":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Funktionen "demo" introducerer dig til alle de kommandoer, du skal bruge for at interagere med Tom i de følgende øvelser.

Kun hvis du er nysgerrig og elsker detaljer:
    Her er den fulde dokumentation for turtle graphics:
    https://docs.python.org/3.3/library/turtle.html

Del 1:
    Skriv en funktion "square", som accepterer en parameter "length".
    Hvis denne funktion kaldes, får skildpadden til at tegne en firkant med en sidelængde på "længde" pixels.

Del 2:
     Færdiggør funktionen "visible", som skal returnere en boolsk værdi,
     der angiver, om skildpadden befinder sig i det synlige område af skærmen.
     Brug denne funktion i de følgende dele af denne øvelse
     til at få skildpadden tilbage til skærmen, når den er vandret væk.

Del 3:
    Skriv en funktion "many_squares" med en for-loop, som kalder square gentagne gange.
    Brug denne funktion til at tegne flere firkanter af forskellig størrelse i forskellige positioner.
    Funktionen skal have nogle parametre. F.eks:
        antal: hvor mange firkanter skal der tegnes?
        størrelse: hvor store er firkanterne?
        afstand: hvor langt væk fra den sidste firkant er den næste firkant placeret?

Del 4:
    Skriv en funktion, der producerer mønstre, der ligner dette:
    https://pixabay.com/vectors/spiral-square-pattern-black-white-154465/

Del 5:
    Skriv en funktion, der producerer mønstre svarende til dette:
    https://www.101computing.net/2d-shapes-using-python-turtle/star-polygons/
    Funktionen skal have en parameter, som påvirker mønsterets form.

Del 6:
    Opret din egen funktion, der producerer et sejt mønster.
    Senere, hvis du har lyst, kan du præsentere dit mønster på storskærmen for de andre.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.

def square(turtle_name, length):
    turtle_name.pendown()
    for i in range(4):
        turtle_name.forward(length)
        turtle_name.right(90)

def visible(turtle_name):  # returns true if both the x- and y-value of the turtle's position are between -480 and 480
    # you will need this: x-value: turtle_name.position()[0]
    # and this:           y-value: turtle_name.position()[1]
    return turtle_name.position()[0] > -480 and turtle_name.position()[0] < 480 and turtle_name.position()[1] > -480 and turtle_name.position()[1] < 480

def many_squares(turtle_name, squares, distances):
    for i in range(len(squares)):
        square(turtle_name, squares[i])
        if (visible(turtle_name) == False):
            turtle_name.home()
        turtle_name.penup()
        turtle_name.forward(distances[i])

def mønster0(turtle_name, length, times, degrees):
    turtle_name.pendown()
    for i in range(times):
        turtle_name.forward(length * i)
        turtle_name.right(degrees)
    turtle_name.penup()

def mønster1(turtle_name, c=5):
    turtle_name.pendown()
    for i in range(c):
        degrees = (3*360/c) # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        turtle_name.left(degrees % 360)
        #turtle_name.right(144 + (5 * (c - 5)))
        turtle_name.forward(100)
    turtle_name.penup()

def egenmønster2(t, times, a, b, c):
    t.pendown()
    for i in range(times):
        t.forward(a * b - c)
        t.right(360/b*c)
        t.forward(b + c / 2 * (a + 6))
        t.left(b * (a - c))
    t.penup()

def demo():  # demonstration of basic turtle commands
    tom = turtle.Turtle()  # create an object named tom of type Turtle

    #egenmønster2(tom, 15, 10, 15, 10)
    #egenmønster2(tom, 15, 10, 16, 10)
    egenmønster2(tom, 15, 10, 16, 11)

    tom.home()  # return to the original position in the middle of the window
    turtle.done()  # keeps the turtle window open after the program is done


demo()
