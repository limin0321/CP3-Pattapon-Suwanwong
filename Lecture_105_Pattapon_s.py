class Vehicle:
    lecenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class co_lor(Vehicle):
    def color(self):
        print("blue")

class Pickup(Vehicle):
    pass;

class Car(Vehicle):
    pass;

class Van(Vehicle):
    pass;

pickup1 = Pickup()
pickup1.turnOnAirConditioner()


car1 = Car()
car1.turnOnAirConditioner()

Van1 =Van()
car1.turnOnAirConditioner()

co_lor1 = co_lor()
co_lor1.color()