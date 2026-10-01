from app.models.parking_slot import ParkingSlot


def backtracking_allocate(
    slots: list[ParkingSlot],
    required_slots: int,
) -> list[ParkingSlot]:
    available_slots = [slot for slot in slots if slot.is_available()]

    if required_slots <= 0:
        return []

    if len(available_slots) < required_slots:
        return []

    best_solution: list[ParkingSlot] = []
    best_cost = float("inf")
    current_solution: list[ParkingSlot] = []

    def backtrack(index: int, current_cost: float) -> None:
        nonlocal best_solution, best_cost

        if len(current_solution) == required_slots:
            if current_cost < best_cost:
                best_cost = current_cost
                best_solution = current_solution.copy()
            return

        if index >= len(available_slots):
            return

        # Choose the current slot
        slot = available_slots[index]
        current_solution.append(slot)

        backtrack(
            index + 1,
            current_cost + slot.distance_from_entrance,
        )

        # Undo the choice
        current_solution.pop()

        # Skip the current slot
        backtrack(index + 1, current_cost)

    backtrack(0, 0.0)

    return best_solution
