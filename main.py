class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def __str__(self):
        return f"Max speed: {self.max_speed} km/h"

class Public_Transport_Vehicle(Vehicle):
    def __init__(self, max_speed, number, depot):
        super().__init__(max_speed)
        self.number = number
        self.depot = depot

    def __str__(self):
        return f"{super().__str__()}, Number: {self.number}, Depot: {self.depot.name}"

class Tram(Public_Transport_Vehicle):
    def __init__(self, max_speed, number, depot, wagons):
        super().__init__(max_speed, number, depot)
        self.wagons = wagons

    def __str__(self):
        return f"Tram {super().__str__()}, Cars: {self.wagons}"

class Bus(Public_Transport_Vehicle):
    def __init__(self, max_speed, number, depot, fuel_consumption):
        super().__init__(max_speed, number, depot)
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return f"Bus {super().__str__()}, Fuel: {self.fuel_consumption} l"

class Depot:
    def __init__(self, name):
        self.name = name
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def __str__(self):
        description = f"{self.name}Vehicles:"
        for vehicle in self.vehicles:
            description += f" {vehicle}"
        return description


tram_depot = Depot("Tram Depot")
bus_depot = Depot("Bus Depot")


vehicles = [
Tram(60, 101, tram_depot, 2),
Tram(55, 102, tram_depot, 3),
Bus(80, 201, bus_depot, 300),
Bus(75, 202, bus_depot, 400),
Bus(70, 203, bus_depot, 350)
]


for vehicle in vehicles:
    vehicle.depot.add_vehicle(vehicle)


print(tram_depot)
print(bus_depot)
