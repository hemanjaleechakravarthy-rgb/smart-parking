from app.models.parking_slot import ParkingSlot
from app.services import process_manager


class FakeProcessPoolExecutor:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False

    def map(self, function, slots):
        return [function(slot) for slot in slots]


def test_calculate_scores_parallel(monkeypatch) -> None:
    monkeypatch.setattr(
        process_manager,
        "ProcessPoolExecutor",
        FakeProcessPoolExecutor,
    )

    slots = [
        ParkingSlot("P01", 10.0),
        ParkingSlot("P02", 20.0),
    ]

    result = process_manager.calculate_scores_parallel(slots)

    assert result[0][0] == "P01"
    assert result[1][0] == "P02"
    assert result[0][1] == 1 / 11
    assert result[1][1] == 1 / 21
