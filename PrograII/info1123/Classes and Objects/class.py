class Car(object):

    def __init__(self, name: str, make: str, year: int, vehicle_type: str):
        """
        :param name: Name of the care
        :param make: Brand(Hyundai/Toyota)
        :param year: Making year
        :param vehicle_type: Sedan/SUV/Hatch
        """

        self.name = name
        self.make = make
        self.year = year
        self.vehicle_type = vehicle_type

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (other.name, other.make, other.year, other.vehicle_type) == (self.name, self.make, self.year, self.vehicle_type)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.make!r}, {self.year!r}, {self.vehicle_type!r})"


car = Car("Jazz", "Honda", 2008, "Hatch")

print(car)
print(car.name)
print(car.make)
print(car.year)
print(car == Car("Jazz", "Honda", 2008, "Hatch"))
