from dataclasses import dataclass


@dataclass
class Vehicle:
    vehicle_number: str
    vehicle_type: str = "car"
    priority: int = 1

    def is_priority_vehicle(self) -> bool:
        return self.priority > 1


@dataclass
class Car(Vehicle):
    vehicle_type: str = "car"


@dataclass
class Bike(Vehicle):
    vehicle_type: str = "bike"


@dataclass
class ElectricVehicle(Vehicle):
    vehicle_type: str = "ev"
