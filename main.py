from app.models.parking_lot import ParkingLot
from app.models.parking_slot import ParkingSlot
from app.models.vehicle import Vehicle
from app.services.parking_manager import ParkingManager


def create_lot() -> ParkingLot:
    lot = ParkingLot()

    lot.add_slot(ParkingSlot("P01", 30.0))
    lot.add_slot(ParkingSlot("P02", 10.0))
    lot.add_slot(ParkingSlot("P03", 20.0))

    return lot


def main() -> None:
    vehicle = Vehicle(
        vehicle_number="AP39AB1234",
        vehicle_type="car",
    )

    manager = ParkingManager(create_lot())

    print("=== Smart Parking Algorithm Demonstration ===")

    print("\nGreedy:")
    print(manager.allocate_greedy(vehicle))

    manager = ParkingManager(create_lot())
    print("\nNearest / Divide and Conquer:")
    print(manager.allocate_nearest())

    manager = ParkingManager(create_lot())
    print("\nDynamic Programming:")
    print(manager.allocate_dynamic(1))

    manager = ParkingManager(create_lot())
    print("\nBacktracking:")
    print(manager.allocate_backtracking(1))

    manager = ParkingManager(create_lot())
    print("\nBranch and Bound:")
    print(manager.allocate_branch_and_bound(1))


if __name__ == "__main__":
    main()