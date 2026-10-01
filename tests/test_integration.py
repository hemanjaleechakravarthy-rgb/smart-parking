from app.models.parking_lot import ParkingLot
from app.models.parking_slot import ParkingSlot
from app.services.parking_manager import ParkingManager
from app.services.parking_strategy import NearestSlotStrategy


def test_parking_allocation_integration() -> None:
    lot = ParkingLot()

    lot.add_slot(ParkingSlot("P01", 30.0))
    lot.add_slot(ParkingSlot("P02", 10.0))
    lot.add_slot(ParkingSlot("P03", 20.0))

    manager = ParkingManager(lot)
    manager.set_strategy(NearestSlotStrategy())

    result = manager.allocate_with_strategy(1)

    assert len(result) == 1
    assert result[0].slot_id == "P02"
    assert result[0].distance_from_entrance == 10.0
