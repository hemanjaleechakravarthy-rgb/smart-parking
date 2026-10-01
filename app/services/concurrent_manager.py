from concurrent.futures import ThreadPoolExecutor

from app.models.parking_lot import ParkingLot
from app.models.parking_slot import ParkingSlot


def check_slot_availability(
    slot: ParkingSlot,
) -> tuple[str, bool]:
    return slot.slot_id, slot.is_available()


def check_slots_concurrently(
    lot: ParkingLot,
) -> list[tuple[str, bool]]:
    with ThreadPoolExecutor(max_workers=4) as executor:
        return list(
            executor.map(
                check_slot_availability,
                lot.slots,
            )
        )
