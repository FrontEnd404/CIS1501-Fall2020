import unittest


# fuel capacity and fuel in tank are in US gallons
class Vehicle:
    def __init__(self,make,model,weight,miles_per_gallon, fuel_capacity, fuel_in_tank):
        self.make = make
        self.model = model
        self.weight = weight
        self.miles_per_gallon = miles_per_gallon
        self.fuel_capacity = fuel_capacity
        self.fuel_in_tank = fuel_in_tank
        global miles_per_gallon1
        miles_per_gallon1 = 100
        global fuel_capacity1
        fuel_capacity1 = 100
        global fuel_in_tank1
        fuel_in_tank1 = 50
    def add_gas(self):
        how_many_gallons_are_added = input("how many gallons of gas are you adding?")
        global fuel_in_tank2
        fuel_in_tank2 = int(fuel_in_tank1) + int(how_many_gallons_are_added)
    def drive(self):
        global fuel_in_tank3
        miles_to_drive = input("how many miles are you driving")
        miles_the_car_can_travel = int(miles_per_gallon1) * int(fuel_in_tank2)
        fuel_in_tank3 = (int(miles_the_car_can_travel) - int(miles_to_drive)) / int(miles_per_gallon1)

fuel_in_tank1 =50
car1 = Vehicle("Ford", "explorer 2077", 5000, 100, 100, fuel_in_tank1)
print("the make of the car is.")
print(car1.make)
print("the model of the car is.")
print(car1.model)
print("the weight of the car is.")
print(car1.weight)
print("the MPG of the car is.")
print(car1.miles_per_gallon)
print("the fuel capacity of the car is.")
print(car1.fuel_capacity)
print("the fuel left in gallons is.")
print(car1.fuel_in_tank)
(car1.add_gas())
print("the fuel left in gallons is now.")
car1= Vehicle("Ford", "explorer 2077", 5000,100,100, fuel_in_tank2)
print(car1.fuel_in_tank)
car1.drive()
car1 = Vehicle("Ford", "explorer 2077", 5000,100,100,fuel_in_tank3)


print("the MPG of the car is.")
print(car1.miles_per_gallon)
print("the fuel capacity of the car is.")
print(car1.fuel_capacity)
print("the fuel left in gallons is now.")
print(car1.fuel_in_tank)

class TestAdd_gas(unittest.TestCase):
    def test_add_gas(self):
        result = stuff.add_gas(20,50)
        self.assertEqual(result,70)

class TestDrive(unittest.TestCase):
    def test_drive(self):
        result = stuff.add_gas(100,100,1000)
        self.assertEqual(result,60)