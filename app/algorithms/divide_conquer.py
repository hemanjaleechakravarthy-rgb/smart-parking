from app.models.parking_slot import ParkingSlot


def find_nearest_slot(
    slots: list[ParkingSlot],
) -> ParkingSlot | None:
    available = [slot for slot in slots if slot.is_available()]

    if not available:
        return None

    def divide(items: list[ParkingSlot]) -> ParkingSlot:
        if len(items) == 1:
            return items[0]

        middle = len(items) // 2

        left_best = divide(items[:middle])
        right_best = divide(items[middle:])

        if left_best.distance_from_entrance <= right_best.distance_from_entrance:
            return left_best

        return right_best

    return divide(available)
