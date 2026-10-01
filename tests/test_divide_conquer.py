from app.algorithms.divide_conquer import find_nearest_slot
from app.models.parking_slot import ParkingSlot


def test_divide_conquer_finds_nearest_slot() -> None:
    slots = [
        ParkingSlot("P01", 40.0),
        ParkingSlot("P02", 15.0),
        ParkingSlot("P03", 25.0),
        ParkingSlot("P04", 5.0),
    ]

    selected = find_nearest_slot(slots)

    assert selected is not None
    assert selected.slot_id == "P04"


def test_divide_conquer_ignores_occupied_slots() -> None:
    slot1 = ParkingSlot("P01", 5.0)
    slot2 = ParkingSlot("P02", 20.0)

    slot1.occupy()

    selected = find_nearest_slot([slot1, slot2])

    assert selected is not None
    assert selected.slot_id == "P02"


def test_divide_conquer_returns_none_when_no_slots() -> None:
    selected = find_nearest_slot([])

    assert selected is None
