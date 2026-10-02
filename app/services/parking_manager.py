from app.algorithms.backtracking import backtracking_allocate
from app.algorithms.branch_bound import branch_and_bound_allocate
from app.algorithms.divide_conquer import find_nearest_slot
from app.algorithms.dynamic_programming import optimal_slot_allocation
from app.algorithms.greedy import greedy_allocate
from app.models.parking_lot import ParkingLot
from app.models.parking_slot import ParkingSlot
from app.models.vehicle import Vehicle
from app.services.parking_strategy import ParkingStrategy
from app.utils.priority_queue import ParkingPriorityQueue


class ParkingManager:
    def __init__(self, parking_lot: ParkingLot) -> None:
        self.parking_lot = parking_lot
        self.strategy: ParkingStrategy | None = None
        self.priority_queue = ParkingPriorityQueue()

    def set_strategy(self, strategy: ParkingStrategy) -> None:
        self.strategy = strategy

    def allocate_with_strategy(
        self,
        required_slots: int,
    ) -> list[ParkingSlot]:
        if self.strategy is None:
            return []

        return self.strategy.allocate(
            self.parking_lot.slots,
            required_slots,
        )

    def allocate_with_priority_queue(self) -> ParkingSlot | None:
        self.priority_queue = ParkingPriorityQueue()

        for slot in self.parking_lot.available_slots():
            self.priority_queue.add(slot)

        return self.priority_queue.get_nearest()

    def allocate_greedy(
        self,
        vehicle: Vehicle,
    ) -> ParkingSlot | None:
        return greedy_allocate(self.parking_lot, vehicle)

    def allocate_nearest(self) -> ParkingSlot | None:
        return find_nearest_slot(self.parking_lot.slots)

    def allocate_dynamic(
        self,
        required_slots: int,
    ) -> list[ParkingSlot]:
        return optimal_slot_allocation(
            self.parking_lot.slots,
            required_slots,
        )

    def allocate_backtracking(
        self,
        required_slots: int,
    ) -> list[ParkingSlot]:
        return backtracking_allocate(
            self.parking_lot.slots,
            required_slots,
        )

    def allocate_branch_and_bound(
        self,
        required_slots: int,
    ) -> list[ParkingSlot]:
        return branch_and_bound_allocate(
            self.parking_lot.slots,
            required_slots,
        )
