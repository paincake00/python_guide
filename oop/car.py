# <CLASS-FOR-EXAMPLE>

class Car:    

    wheels_count = 4    # class_variable

    def __init__(self, make, model, year, color):
        self.make = make    # instance_variable
        self.model = model  # instance_variable
        self.year = year    # instance_variable
        self.color = color  # instance_variable

    def info(self):
        print("Info about car:\n make: {}\n model: {}\n year: {}\n color: {}".format(self.make, self.model, self.year, self.color))

    def drive(self):
        print("{make} {model} is driving".format(make=self.make, model=self.model))

    def stop(self):
        print("{make} {model} is stopped".format(make=self.make, model=self.model))