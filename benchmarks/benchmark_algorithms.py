import time

from app.algorithms.backtracking import backtracking_allocate
from app.algorithms.branch_bound import branch_and_bound_allocate
from app.algorithms.divide_conquer import find_nearest_slot
from app.algorithms.dynamic_programming import optimal_slot_allocation
from app.algorithms.greedy import greedy_allocate
from app.models.parking_lot import ParkingLot
from app.models.parking_slot import ParkingSlot
from app.models.vehicle import Vehicle


def create_slots(size: int) -> list[ParkingSlot]:
    return [
        ParkingSlot(
            slot_id=f"P{i:03d}",
            distance_from_entrance=float(i),
        )
        for i in range(1, size + 1)
    ]


def measure(name: str, function, repetitions: int = 10) -> float:
    total_time = 0.0

    for _ in range(repetitions):
        start = time.perf_counter()
        function()
        end = time.perf_counter()

        total_time += (end - start) * 1000

    average_time = total_time / repetitions

    print(f"{name:<25} {average_time:.4f} ms")
    return average_time


def benchmark(size: int) -> None:
    print(f"\n--- Parking Lot Size: {size} ---")

    vehicle = Vehicle("AP39AB1234", "car")

    measure(
        "Greedy",
        lambda: greedy_allocate(
            ParkingLot(create_slots(size)),
            vehicle,
        ),
    )

    measure(
        "Divide & Conquer",
        lambda: find_nearest_slot(create_slots(size)),
    )

    measure(
        "Dynamic Programming",
        lambda: optimal_slot_allocation(
            create_slots(size),
            1,
        ),
    )

    measure(
        "Backtracking",
        lambda: backtracking_allocate(
            create_slots(size),
            5,
        ),
    )

    measure(
        "Branch & Bound",
        lambda: branch_and_bound_allocate(
            create_slots(size),
            5,
        ),
    )


def main() -> None:
    print("=== Smart Parking Performance Benchmark ===")

    for size in [5, 10, 15, 20, 25]:
        benchmark(size)


if __name__ == "__main__":
    main()
