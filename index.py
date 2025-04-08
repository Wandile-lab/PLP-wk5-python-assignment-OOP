# Assignment 1

class SmartPhone:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def trade(self):
        print(f"The next phone I plan to buy is the {self.name} {self.model}, in the {self.color} color.")

class iPhone(SmartPhone):
    def trade(self):
        print(f"Trading in for an iPhone {self.model} in a{self.color} color.")

# Assignment 2
class  Car:
    def move(self):
        return "The car drives to it's next destination"
    
class Plane:
    def move(self):
        return "The plane flies to it's next destination"
    
for vehicle in [Car(), Plane()]:
    print(vehicle.move())