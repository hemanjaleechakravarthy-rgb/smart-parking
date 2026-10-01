import asyncio

from app.models.parking_slot import ParkingSlot
from app.services.async_manager import check_slots_async


def test_check_slots_async() -> None:
    slots = [
        ParkingSlot("P01", 10.0),
        ParkingSlot("P02", 20.0),
        ParkingSlot("P03", 30.0),
    ]

    result = asyncio.run(check_slots_async(slots))

    assert len(result) == 3
    assert result[0] == ("P01", True)
    assert result[1] == ("P02", True)
    assert result[2] == ("P03", True)
