import turtle
import cv2
import sys
import random
import math

#IMAGE_PIXEL_SIZE = 15
IMAGE_PIXEL_SIZE = 1

# todo make this not bad haha
# it would probably be faster to make it draw like scan lines in old crt tvs
def drawImg(filename, bob):
    startpos = bob.position()
    image = cv2.imread(filename)
    turtle.tracer(0, 0)
    turtle.colormode(255)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            bob.color(image[x, y])
            bob.begin_fill()
            for i in range(4):
                bob.forward(IMAGE_PIXEL_SIZE)
                bob.right(90)
            bob.end_fill()
            bob.forward(IMAGE_PIXEL_SIZE)
        bob.penup()
        bob.setpos(startpos)
        bob.right(90)
        bob.forward(IMAGE_PIXEL_SIZE)
        bob.left(90)
        bob.pendown()
        turtle.update()

def distance(pos1, pos2):  # calculate the distance between 2 points with the Pythagorean equation
    delta_x = pos1[0] - pos2[0]
    delta_y = pos1[1] - pos2[1]
    return math.sqrt(delta_x ** 2 + delta_y ** 2)

def getangle(start_position, end_position):
    # returns the direction from start_position to end_position in degrees
    # 0° is east (plus x-axis), which is also the direction of each turtle at the beginning of each hunt.
    # 90° is south (minus y-axis), 180° is west (minus x-axis), 270° is north (plus y-axis)
    delta_x = end_position[0] - start_position[0]
    delta_y = end_position[1] - start_position[1]
    angle = math.atan2(delta_y, delta_x) * 180 / math.pi
    if delta_y < 0:
        return -angle
    else:
        return 360 - angle

def coolPattern(bob, dub):
    try:
        turtle.colormode(255)

        if dub:
            bob.penup()
            bob.setpos(random.randint(-turtle.screensize()[0], turtle.screensize()[0]), random.randint(-turtle.screensize()[1], turtle.screensize()[1]))
            bob.pendown()
            bob.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        d = distance((-turtle.screensize()[0], -turtle.screensize()[1]), turtle.screensize())

        active_bobs = []

        while(True):
            weights = []

            for i in range(10):
                x = math.cos(i / math.pi)
                y = math.sin(i / math.pi)
                pos = bob.pos() + (x, y) * 100

                num = (d - pos[0]) + (d - pos[1])
                for j in range(int(num)):
                    weights.append(pos)

            target = weights[random.randint(0, len(weights))]
            target_angle = getangle(bob.pos(), target)

            bob.right(target_angle)
            bob.left(25)
            for j in range(int(distance(bob.pos(), pos) * 10)):
                bob.forward(10 + random.randint(-5, 5))
                bob.right(12.2 + random.randint(-5, 5))
                bob.pensize((d - distance(bob.pos(), pos)) * 0.05)
                if dub:
                    bob.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            if dub:
                newbob = turtle.Turtle()
                newbob.speed(0)
                newbob.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                active_bobs.append(newbob)
                for b in active_bobs:
                    coolPattern(b, False)
                turtle.update()
            else:
                if abs(bob.pos()[0]) > turtle.screensize()[0] - 10 or abs(bob.pos()[1]) > turtle.screensize()[1] - 10:
                    bob.penup()
                    bob.hideturtle()
                    bob.setpos(0,0)
                return
    except:
        # too lazy to fix daksjfdkowsaijfdewis
        turtle.done()
        while(True):
            pass

Bob = turtle.Turtle()
Bob.speed(0)

#drawImg(sys.argv[1], Bob)
#drawImg("D:\Pycharm Projects\stuff\c1f579a5d38eb9d269d7ea030dafee63.jpg", Bob)

turtle.tracer(0,0)
coolPattern(Bob, True)

turtle.mainloop()
