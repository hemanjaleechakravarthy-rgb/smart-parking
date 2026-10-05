from app.models.parking_slot import ParkingSlot


def branch_and_bound_allocate(
    slots: list[ParkingSlot],
    required_slots: int,
    vehicle_type: str | None = None,
    priority_required: bool = False,
    ev_charging_required: bool = False,
) -> list[ParkingSlot]:
    """
    Allocate parking slots using Branch and Bound.
    """

    available_slots = [
        slot
        for slot in slots
        if slot.is_available()
        and (vehicle_type is None or slot.vehicle_type == vehicle_type)
        and (not priority_required or slot.priority)
        and (not ev_charging_required or slot.ev_charging)
    ]

    if required_slots <= 0:
        return []

    if len(available_slots) < required_slots:
        return []

    available_slots.sort(key=lambda slot: slot.distance_from_entrance)

    best_solution: list[ParkingSlot] = []
    best_cost = float("inf")

    def search(
        index: int,
        selected: list[ParkingSlot],
        current_cost: float,
    ) -> None:
        nonlocal best_solution, best_cost

        if len(selected) == required_slots:
            if current_cost < best_cost:
                best_cost = current_cost
                best_solution = selected.copy()

            return

        if index >= len(available_slots):
            return

        remaining_needed = required_slots - len(selected)

        remaining_slots = len(available_slots) - index

        if remaining_slots < remaining_needed:
            return

        next_slot = available_slots[index]

        new_cost = current_cost + next_slot.distance_from_entrance

        if new_cost < best_cost:
            selected.append(next_slot)

            search(
                index + 1,
                selected,
                new_cost,
            )

            selected.pop()

        search(
            index + 1,
            selected,
            current_cost,
        )

    search(0, [], 0.0)

    return best_solution
