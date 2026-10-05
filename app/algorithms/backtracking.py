from app.models.parking_slot import ParkingSlot


def backtracking_allocate(
    slots: list[ParkingSlot],
    required_slots: int,
    vehicle_type: str | None = None,
    priority_required: bool = False,
    ev_charging_required: bool = False,
) -> list[ParkingSlot]:
    """
    Allocate parking slots using Backtracking.
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

    best_solution: list[ParkingSlot] = []
    best_cost = float("inf")
    current_solution: list[ParkingSlot] = []

    def backtrack(
        index: int,
        current_cost: float,
    ) -> None:
        nonlocal best_solution, best_cost

        if len(current_solution) == required_slots:
            if current_cost < best_cost:
                best_cost = current_cost
                best_solution = current_solution.copy()

            return

        if index >= len(available_slots):
            return

        slot = available_slots[index]

        current_solution.append(slot)

        backtrack(
            index + 1,
            current_cost + slot.distance_from_entrance,
        )

        current_solution.pop()

        backtrack(
            index + 1,
            current_cost,
        )

    backtrack(0, 0.0)

    return best_solution
