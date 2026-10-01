from app.algorithms.greedy import greedy_allocate
from app.models.parking_lot import ParkingLot
from app.models.parking_slot import ParkingSlot
from app.models.vehicle import Vehicle


def test_greedy_selects_nearest_slot() -> None:
    lot = ParkingLot()

    lot.add_slot(ParkingSlot("P01", 30.0))
    lot.add_slot(ParkingSlot("P02", 10.0))
    lot.add_slot(ParkingSlot("P03", 20.0))

    vehicle = Vehicle("AP39AB1234", "car")

    selected = greedy_allocate(lot, vehicle)

    assert selected is not None
    assert selected.slot_id == "P02"
    assert selected.occupied is True


def test_backtracking_with_zero_required_slots() -> None:
    from app.algorithms.backtracking import backtracking_allocate
    from app.models.parking_slot import ParkingSlot

    slots = [
        ParkingSlot("P01", 10.0),
        ParkingSlot("P02", 20.0),
    ]

    result = backtracking_allocate(slots, 0)

    assert result == []


def test_greedy_returns_none_when_all_slots_occupied() -> None:
    from app.algorithms.greedy import greedy_allocate
    from app.models.parking_lot import ParkingLot
    from app.models.parking_slot import ParkingSlot
    from app.models.vehicle import Car

    lot = ParkingLot()
    lot.add_slot(
        ParkingSlot(
            "P01",
            10.0,
            vehicle_type="car",
            occupied=True,
        )
    )

    vehicle = Car("AP39AB1234")

    result = greedy_allocate(lot, vehicle)

    assert result is None
