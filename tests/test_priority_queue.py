from app.models.parking_slot import ParkingSlot
from app.utils.priority_queue import ParkingPriorityQueue


def test_priority_queue_returns_nearest_slot() -> None:
    queue = ParkingPriorityQueue()

    queue.add(ParkingSlot("P01", 30.0))
    queue.add(ParkingSlot("P02", 10.0))
    queue.add(ParkingSlot("P03", 20.0))

    nearest = queue.get_nearest()

    assert nearest is not None
    assert nearest.slot_id == "P02"
    assert nearest.distance_from_entrance == 10.0


def test_priority_queue_size_and_empty() -> None:
    queue = ParkingPriorityQueue()

    assert queue.is_empty()
    assert queue.size() == 0

    queue.add(ParkingSlot("P01", 15.0))

    assert not queue.is_empty()
    assert queue.size() == 1


def test_priority_queue_returns_none_when_empty() -> None:
    queue = ParkingPriorityQueue()

    assert queue.get_nearest() is None
