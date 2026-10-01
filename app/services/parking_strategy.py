from abc import ABC, abstractmethod

from app.models.parking_slot import ParkingSlot


class ParkingStrategy(ABC):
    @abstractmethod
    def allocate(
        self,
        slots: list[ParkingSlot],
        required_slots: int,
    ) -> list[ParkingSlot]:
        pass


class NearestSlotStrategy(ParkingStrategy):
    def allocate(
        self,
        slots: list[ParkingSlot],
        required_slots: int,
    ) -> list[ParkingSlot]:
        available = [slot for slot in slots if slot.is_available()]

        available.sort(key=lambda slot: slot.distance_from_entrance)

        return available[:required_slots]
