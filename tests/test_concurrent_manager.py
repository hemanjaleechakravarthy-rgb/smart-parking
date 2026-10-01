from app.models.parking_lot import ParkingLot
from app.models.parking_slot import ParkingSlot
from app.services.concurrent_manager import check_slots_concurrently


def test_check_slots_concurrently() -> None:
    lot = ParkingLot()

    slot1 = ParkingSlot("P01", 10.0)
    slot2 = ParkingSlot("P02", 20.0)
    slot3 = ParkingSlot("P03", 30.0)

    slot2.occupy()

    lot.add_slot(slot1)
    lot.add_slot(slot2)
    lot.add_slot(slot3)

    result = check_slots_concurrently(lot)

    assert result == [
        ("P01", True),
        ("P02", False),
        ("P03", True),
    ]
