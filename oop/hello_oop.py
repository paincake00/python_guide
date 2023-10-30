from car import Car     # import class "Car" from module with name "car"

first_car = Car("Ford", "RS200 Evolution", "1986", "white")
second_car = Car("Ford", "Mustang Shelby GT500", "2008", "blue")

first_car.info()
first_car.drive()
print("-" * 40)

second_car.info()
second_car.stop()
print("-" * 40)

print("Count of wheels: " + str(Car.wheels_count))