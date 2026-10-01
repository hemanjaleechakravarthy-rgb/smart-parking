from app.algorithms.branch_bound import branch_and_bound_allocate
from app.models.parking_slot import ParkingSlot


def test_branch_and_bound_finds_best_allocation() -> None:
    slots = [
        ParkingSlot("P01", 30.0),
        ParkingSlot("P02", 10.0),
        ParkingSlot("P03", 20.0),
        ParkingSlot("P04", 40.0),
    ]

    selected = branch_and_bound_allocate(slots, 2)

    assert len(selected) == 2
    assert {slot.slot_id for slot in selected} == {"P02", "P03"}


def test_branch_and_bound_ignores_occupied_slots() -> None:
    slot1 = ParkingSlot("P01", 5.0)
    slot2 = ParkingSlot("P02", 20.0)
    slot3 = ParkingSlot("P03", 30.0)

    slot1.occupy()

    selected = branch_and_bound_allocate(
        [slot1, slot2, slot3],
        2,
    )

    assert len(selected) == 2
    assert {slot.slot_id for slot in selected} == {"P02", "P03"}


def test_branch_and_bound_returns_empty_if_not_enough_slots() -> None:
    slots = [
        ParkingSlot("P01", 10.0),
    ]

    selected = branch_and_bound_allocate(slots, 2)

    assert selected == []


def test_branch_and_bound_zero_required_slots() -> None:
    from app.algorithms.branch_bound import branch_and_bound_allocate
    from app.models.parking_slot import ParkingSlot

    slots = [
        ParkingSlot("P01", 10.0),
        ParkingSlot("P02", 20.0),
    ]

    result = branch_and_bound_allocate(slots, 0)

    assert result == []
