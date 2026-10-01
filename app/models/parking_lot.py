from dataclasses import dataclass, field

from app.models.parking_slot import ParkingSlot
from app.models.vehicle import Vehicle


@dataclass
class ParkingLot:
    slots: list[ParkingSlot] = field(default_factory=list)

    def add_slot(self, slot: ParkingSlot) -> None:
        self.slots.append(slot)

    def available_slots(self) -> list[ParkingSlot]:
        return [slot for slot in self.slots if slot.is_available()]

    def total_slots(self) -> int:
        return len(self.slots)

    def available_count(self) -> int:
        return len(self.available_slots())

    def assign_vehicle(
        self,
        vehicle: Vehicle,
        slot: ParkingSlot,
    ) -> bool:
        if not slot.is_available():
            return False

        if slot.vehicle_type != vehicle.vehicle_type:
            return False

        slot.occupy()
        return True
