from dataclasses import dataclass


@dataclass
class Car:
    name: str
    make: str
    year: int
    vehicle_type: str


car = Car("Jazz", "Honda", 2008, "Hatch")
print(car)
print(car.name)
print(car.make)
print(car.year)
print(car == Car("Jazz", "Honda", 2008, "Hatch"))
