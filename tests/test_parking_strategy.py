from app.models.parking_slot import ParkingSlot
from app.services.parking_strategy import NearestSlotStrategy


def test_nearest_slot_strategy() -> None:
    slots = [
        ParkingSlot("P01", 30.0),
        ParkingSlot("P02", 10.0),
        ParkingSlot("P03", 20.0),
    ]

    strategy = NearestSlotStrategy()
    result = strategy.allocate(slots, 2)

    assert [slot.slot_id for slot in result] == ["P02", "P03"]
