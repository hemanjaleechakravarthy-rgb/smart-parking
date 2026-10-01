from app.models.parking_slot import ParkingSlot
from app.services.parking_repository import ParkingRepository


def test_parking_repository() -> None:
    repository = ParkingRepository()

    slot1 = ParkingSlot("P01", 10.0)
    slot2 = ParkingSlot("P02", 20.0)

    repository.add(slot1)
    repository.add(slot2)

    assert repository.get("P01") == slot1
    assert len(repository.get_all()) == 2

    repository.remove("P01")

    assert repository.get("P01") is None
    assert len(repository.get_all()) == 1
