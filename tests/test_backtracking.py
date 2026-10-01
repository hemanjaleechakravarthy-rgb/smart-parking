from app.algorithms.backtracking import backtracking_allocate
from app.models.parking_slot import ParkingSlot


def test_backtracking_allocates_required_slots() -> None:
    slots = [
        ParkingSlot("P01", 10.0),
        ParkingSlot("P02", 20.0),
        ParkingSlot("P03", 30.0),
    ]

    selected = backtracking_allocate(slots, 2)

    assert len(selected) == 2
    assert selected[0].slot_id == "P01"
    assert selected[1].slot_id == "P02"


def test_backtracking_ignores_occupied_slots() -> None:
    slot1 = ParkingSlot("P01", 10.0)
    slot2 = ParkingSlot("P02", 20.0)

    slot1.occupy()

    selected = backtracking_allocate([slot1, slot2], 1)

    assert len(selected) == 1
    assert selected[0].slot_id == "P02"


def test_backtracking_returns_empty_when_not_enough_slots() -> None:
    slots = [
        ParkingSlot("P01", 10.0),
    ]

    selected = backtracking_allocate(slots, 2)

    assert selected == []


def test_backtracking_index_exhausted() -> None:
    from app.algorithms.backtracking import backtracking_allocate
    from app.models.parking_slot import ParkingSlot

    slots = [
        ParkingSlot("P01", 10.0),
    ]

    result = backtracking_allocate(slots, 2)

    assert result == []
