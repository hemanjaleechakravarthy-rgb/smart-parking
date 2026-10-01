from app.algorithms.dynamic_programming import optimal_slot_allocation
from app.models.parking_slot import ParkingSlot


def test_optimal_slot_allocation() -> None:
    slots = [
        ParkingSlot("P01", 30.0),
        ParkingSlot("P02", 10.0),
        ParkingSlot("P03", 20.0),
    ]

    result = optimal_slot_allocation(slots, 2)

    assert len(result) == 2
    assert {slot.slot_id for slot in result} == {"P02", "P03"}


def test_optimal_slot_allocation_zero_required() -> None:
    slots = [
        ParkingSlot("P01", 10.0),
        ParkingSlot("P02", 20.0),
    ]

    result = optimal_slot_allocation(slots, 0)

    assert result == []


def test_optimal_slot_allocation_more_than_available() -> None:
    slots = [
        ParkingSlot("P01", 10.0),
        ParkingSlot("P02", 20.0),
    ]

    result = optimal_slot_allocation(slots, 3)

    assert result == []


def test_optimal_slot_allocation_occupied_slot() -> None:
    slots = [
        ParkingSlot("P01", 10.0, occupied=True),
        ParkingSlot("P02", 20.0),
        ParkingSlot("P03", 30.0),
    ]

    result = optimal_slot_allocation(slots, 2)

    assert len(result) == 2
    assert {slot.slot_id for slot in result} == {"P02", "P03"}
