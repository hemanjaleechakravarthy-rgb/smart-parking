from app.models.parking_slot import ParkingSlot


class ParkingRepository:
    def __init__(self) -> None:
        self.slots: dict[str, ParkingSlot] = {}

    def add(self, slot: ParkingSlot) -> None:
        self.slots[slot.slot_id] = slot

    def get(self, slot_id: str) -> ParkingSlot | None:
        return self.slots.get(slot_id)

    def get_all(self) -> list[ParkingSlot]:
        return list(self.slots.values())

    def remove(self, slot_id: str) -> None:
        self.slots.pop(slot_id, None)
