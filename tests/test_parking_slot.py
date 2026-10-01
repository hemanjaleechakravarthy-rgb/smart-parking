from app.models.parking_slot import ParkingSlot


def test_new_slot_is_available() -> None:
    slot = ParkingSlot(slot_id="P01", distance_from_entrance=10.0)

    assert slot.is_available() is True


def test_occupied_slot_is_not_available() -> None:
    slot = ParkingSlot(slot_id="P01", distance_from_entrance=10.0)

    slot.occupy()

    assert slot.is_available() is False


def test_released_slot_is_available() -> None:
    slot = ParkingSlot(slot_id="P01", distance_from_entrance=10.0)

    slot.occupy()
    slot.release()

    assert slot.is_available() is True
