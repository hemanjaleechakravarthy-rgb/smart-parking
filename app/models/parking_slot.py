from dataclasses import dataclass


@dataclass
class ParkingSlot:
    slot_id: str
    distance_from_entrance: float
    vehicle_type: str = "car"
    occupied: bool = False
    priority: bool = False
    ev_charging: bool = False

    def is_available(self) -> bool:
        return not self.occupied

    def occupy(self) -> None:
        self.occupied = True

    def release(self) -> None:
        self.occupied = False
