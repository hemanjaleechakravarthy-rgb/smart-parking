from app.models.parking_slot import ParkingSlot
from app.utils.functional import (
    apply_to_slots,
    calculate_average_distance,
    get_available_slots,
    slot_id_generator,
)


def test_get_available_slots() -> None:
    slot1 = ParkingSlot("P01", 10.0)
    slot2 = ParkingSlot("P02", 20.0)

    slot1.occupy()

    available = get_available_slots([slot1, slot2])

    assert len(available) == 1
    assert available[0].slot_id == "P02"


def test_calculate_average_distance() -> None:
    slots = [
        ParkingSlot("P01", 10.0),
        ParkingSlot("P02", 20.0),
        ParkingSlot("P03", 30.0),
    ]

    assert calculate_average_distance(slots) == 20.0


def test_higher_order_function() -> None:
    slots = [
        ParkingSlot("P01", 10.0),
        ParkingSlot("P02", 20.0),
    ]

    result = apply_to_slots(
        slots,
        lambda slot: f"Slot {slot.slot_id}",
    )

    assert result == ["Slot P01", "Slot P02"]


def test_slot_id_generator() -> None:
    slots = [
        ParkingSlot("P01", 10.0),
        ParkingSlot("P02", 20.0),
    ]

    generator = slot_id_generator(slots)

    assert next(generator) == "P01"
    assert next(generator) == "P02"


def test_calculate_average_distance_empty() -> None:
    result = calculate_average_distance([])

    assert result == 0.0
