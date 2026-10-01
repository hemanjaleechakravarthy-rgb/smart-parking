from concurrent.futures import ProcessPoolExecutor

from app.models.parking_slot import ParkingSlot


def calculate_slot_score(slot: ParkingSlot) -> tuple[str, float]:
    score = 1 / (slot.distance_from_entrance + 1)
    return slot.slot_id, score


def calculate_scores_parallel(
    slots: list[ParkingSlot],
) -> list[tuple[str, float]]:
    with ProcessPoolExecutor() as executor:
        return list(
            executor.map(
                calculate_slot_score,
                slots,
            )
        )
