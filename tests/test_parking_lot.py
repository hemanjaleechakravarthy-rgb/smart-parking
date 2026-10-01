from app.models.parking_lot import ParkingLot
from app.models.parking_slot import ParkingSlot


def test_parking_lot_counts_slots() -> None:
    lot = ParkingLot()

    lot.add_slot(ParkingSlot("P01", 10.0))
    lot.add_slot(ParkingSlot("P02", 20.0))
    lot.add_slot(ParkingSlot("P03", 30.0))

    assert lot.total_slots() == 3
    assert lot.available_count() == 3


def test_parking_lot_counts_available_slots() -> None:
    lot = ParkingLot()

    slot1 = ParkingSlot("P01", 10.0)
    slot2 = ParkingSlot("P02", 20.0)

    lot.add_slot(slot1)
    lot.add_slot(slot2)

    slot1.occupy()

    assert lot.total_slots() == 2
    assert lot.available_count() == 1


def test_assign_vehicle() -> None:
    from app.models.vehicle import Car

    lot = ParkingLot()
    slot = ParkingSlot("P01", 10.0)
    lot.add_slot(slot)

    vehicle = Car("AP39AB1234")

    assert lot.assign_vehicle(vehicle, slot) is True
    assert slot.is_available() is False


def test_assign_vehicle_rejects_wrong_type() -> None:
    from app.models.vehicle import Bike

    lot = ParkingLot()
    slot = ParkingSlot("P01", 10.0)
    lot.add_slot(slot)

    vehicle = Bike("AP39CD5678")

    assert lot.assign_vehicle(vehicle, slot) is False
    assert slot.is_available() is True


def test_assign_vehicle_rejects_occupied_slot() -> None:
    from app.models.vehicle import Car

    lot = ParkingLot()
    slot = ParkingSlot("P01", 10.0, occupied=True)
    lot.add_slot(slot)

    vehicle = Car("AP39AB1234")

    assert lot.assign_vehicle(vehicle, slot) is False
