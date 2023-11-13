"""
Konstruktor:

Nu bruger vi en konstruktor til at definere bilerne og deres attributter på en mere elegant måde.

Inspicer følgende kode i detaljer. Find ud af, hvad hver række kode gør.
F.eks. ved at ændre koden en smule og derefter køre/debugge programmet.

Derefter går du videre med den næste fil."""


class Vehicle:  # this starts the definition of a class

    def __init__(self, wheels, max_speed):
        # in python the constructor of a class is always called __init__
        # a constructor creates an instance/object of a class
        self.wheels = wheels  # wheels is called an attribute. A attribute is a variable that belongs to an object of a class.
        self.max_speed = max_speed  # Another attribute.

    def drive(self):  # This is a method. A method is a function that belongs to a class.
        print("WROOOOOOOOM!")


car1 = Vehicle(4, 160)  # car1 is now defined as an instance/object of type Vehicle. Also its attributes are already defined.
car2 = Vehicle(8, 100)

print("wheels", car1.wheels, "maximum speed", car1.max_speed)  # print out the attributes of car1
print("wheels", car2.wheels, "maximum speed", car2.max_speed)  # print out the attributes of car2
car1.drive()  # the method drive of the class Vehicle is called on the object car1
