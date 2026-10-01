from app.models.parking_slot import ParkingSlot
from app.services.process_manager import calculate_scores_parallel


def test_calculate_scores_parallel() -> None:
    slots = [
        ParkingSlot("P01", 10.0),
        ParkingSlot("P02", 20.0),
        ParkingSlot("P03", 30.0),
    ]

    result = calculate_scores_parallel(slots)

    assert len(result) == 3
    assert result[0][0] == "P01"
    assert result[0][1] > 0
