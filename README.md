# Public Transport Vehicle Management System

This project is designed to manage public transport vehicles, including trams and buses, within a depot system. It provides a basic framework for creating and managing vehicles, assigning them to depots, and displaying their details.

## Features

- **Vehicle Classes**: The system includes classes for `Tram` and `Bus`, each with their own attributes and methods.
- **Depot Management**: Depots are represented by the `Depot` class, which can hold multiple vehicles.
- **Vehicle Assignment**: Vehicles are assigned to specific depots during creation.
- **Information Display**: The system can display detailed information about each vehicle and depot.

## Usage

1. **Create Depots**: Initialize depot objects for trams and buses.
2. **Create Vehicles**: Create tram or bus objects, specifying their attributes and assigning them to a depot.
3. **Display Information**: Use the `__str__` method to print detailed information about vehicles and depots.

## Code Structure

The project is structured into several classes:
- `Vehicle`: Base class for all vehicles.
- `PublicTransportVehicle`: Intermediate class with common attributes for public transport vehicles.
- `Tram` and `Bus`: Derived classes with specific attributes.
- `Depot`: Class representing a depot that can hold vehicles.

## Requirements

- Python 3.x

## Example Usage

Create depots
tram_depot = Depot("Tram Depot")
bus_depot = Depot("Bus Depot")

Create vehicles
vehicles = [
Tram(60, 101, tram_depot, 2),
Tram(55, 102, tram_depot, 3),
Bus(80, 201, bus_depot, 300),
Bus(75, 202, bus_depot, 400),
Bus(70, 203, bus_depot, 350)
]

Add vehicles to depots and display information
for vehicle in vehicles:
vehicle.depot.add_vehicle(vehicle)

print(tram_depot)
print(bus_depot)