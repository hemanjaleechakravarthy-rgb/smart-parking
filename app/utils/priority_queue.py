import heapq

from app.models.parking_slot import ParkingSlot


class ParkingPriorityQueue:
    """Min-heap based priority queue for parking slots."""

    def __init__(self) -> None:
        self._heap: list[tuple[float, str, ParkingSlot]] = []

    def add(self, slot: ParkingSlot) -> None:
        heapq.heappush(
            self._heap,
            (slot.distance_from_entrance, slot.slot_id, slot),
        )

    def get_nearest(self) -> ParkingSlot | None:
        if not self._heap:
            return None

        return heapq.heappop(self._heap)[2]

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def size(self) -> int:
        return len(self._heap)
