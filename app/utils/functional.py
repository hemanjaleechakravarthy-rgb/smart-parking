from collections.abc import Callable, Iterator

from app.models.parking_slot import ParkingSlot


def get_available_slots(
    slots: list[ParkingSlot],
) -> list[ParkingSlot]:
    return [slot for slot in slots if slot.is_available()]


def calculate_average_distance(
    slots: list[ParkingSlot],
) -> float:
    if not slots:
        return 0.0

    total_distance = sum(slot.distance_from_entrance for slot in slots)

    return total_distance / len(slots)


def apply_to_slots(
    slots: list[ParkingSlot],
    operation: Callable[[ParkingSlot], str],
) -> list[str]:
    return [operation(slot) for slot in slots]


def slot_id_generator(
    slots: list[ParkingSlot],
) -> Iterator[str]:
    for slot in slots:
        yield slot.slot_id
