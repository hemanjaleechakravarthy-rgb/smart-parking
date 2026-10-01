from app.models.parking_lot import ParkingLot
from app.models.parking_slot import ParkingSlot
from app.models.vehicle import Vehicle
from app.services.parking_manager import ParkingManager


def create_test_lot() -> ParkingLot:
    lot = ParkingLot()

    lot.add_slot(ParkingSlot("P01", 30.0))
    lot.add_slot(ParkingSlot("P02", 10.0))
    lot.add_slot(ParkingSlot("P03", 20.0))

    return lot


def test_manager_greedy_allocation() -> None:
    lot = create_test_lot()
    manager = ParkingManager(lot)

    vehicle = Vehicle("AP39AB1234", "car")

    selected = manager.allocate_greedy(vehicle)

    assert selected is not None
    assert selected.slot_id == "P02"


def test_manager_nearest_allocation() -> None:
    lot = create_test_lot()
    manager = ParkingManager(lot)

    selected = manager.allocate_nearest()

    assert selected is not None
    assert selected.slot_id == "P02"


def test_manager_dynamic_allocation() -> None:
    lot = create_test_lot()
    manager = ParkingManager(lot)

    selected = manager.allocate_dynamic(2)

    assert len(selected) == 2


def test_manager_backtracking_allocation() -> None:
    lot = create_test_lot()
    manager = ParkingManager(lot)

    selected = manager.allocate_backtracking(2)

    assert len(selected) == 2


def test_manager_branch_and_bound_allocation() -> None:
    lot = create_test_lot()
    manager = ParkingManager(lot)

    selected = manager.allocate_branch_and_bound(2)

    assert len(selected) == 2


def test_strategy_allocation() -> None:
    from app.services.parking_strategy import NearestSlotStrategy

    lot = ParkingLot()
    lot.add_slot(ParkingSlot("P01", 30.0))
    lot.add_slot(ParkingSlot("P02", 10.0))

    manager = ParkingManager(lot)

    assert manager.allocate_with_strategy(1) == []

    manager.set_strategy(NearestSlotStrategy())

    result = manager.allocate_with_strategy(1)

    assert [slot.slot_id for slot in result] == ["P02"]
