# <INHERITANCE: basic, multilevel; SUPER()>

# First Example

class Status:
     working_condition = True

class Vehicle(Status):
    def __init__(self, company, model, year, color):
        self.company = company
        self.model = model
        self.year = year
        self.color = color

class Car(Vehicle):
    def __init__(self, company, model, year, color, car_type):
        super().__init__(company, model, year, color)
        self.car_type = car_type

print("-"*20 + "First_Example" + "-"*20)
car = Car("Nissan", "GT-R R35", "2009", "gray", "sport car")
print(f"I have a {car.company} model {car.model}.\nWorking status: {Car.working_condition}")

# Second Example

class Organism:

    alive = True

class Animal(Organism):

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " is eating")

    def sleep(self):
        print(self.name + " is sleeping")    

class Dog(Animal):

    def bark(self):
        print(self.name + " is barking")

print("-"*20 + "Second_Example" + "-"*20)
dog = Dog("Rex")
print("Are you alive?: " + str(Dog.alive))
dog.bark()