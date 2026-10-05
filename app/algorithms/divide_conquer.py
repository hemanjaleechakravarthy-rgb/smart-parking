from app.models.parking_slot import ParkingSlot


def find_nearest_slot(
    slots: list[ParkingSlot],
    required_slots: int = 1,
    vehicle_type: str | None = None,
    priority_required: bool = False,
    ev_charging_required: bool = False,
) -> ParkingSlot | list[ParkingSlot] | None:
    """
    Find nearest parking slots using Divide and Conquer.
    """

    available = [
        slot
        for slot in slots
        if slot.is_available()
        and (vehicle_type is None or slot.vehicle_type == vehicle_type)
        and (not priority_required or slot.priority)
        and (not ev_charging_required or slot.ev_charging)
    ]

    if required_slots <= 0 or not available:
        return None

    def divide(
        items: list[ParkingSlot],
    ) -> list[ParkingSlot]:

        if len(items) <= 1:
            return items.copy()

        middle = len(items) // 2

        left_best = divide(items[:middle])
        right_best = divide(items[middle:])

        merged: list[ParkingSlot] = []

        left_index = 0
        right_index = 0

        while left_index < len(left_best) and right_index < len(right_best):
            if (
                left_best[left_index].distance_from_entrance
                <= right_best[right_index].distance_from_entrance
            ):
                merged.append(left_best[left_index])
                left_index += 1
            else:
                merged.append(right_best[right_index])
                right_index += 1

        merged.extend(left_best[left_index:])
        merged.extend(right_best[right_index:])

        return merged

    sorted_slots = divide(available)

    selected_slots = sorted_slots[:required_slots]

    if not selected_slots:
        return None

    if required_slots == 1:
        return selected_slots[0]

    return selected_slots
