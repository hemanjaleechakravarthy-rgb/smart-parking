from app.models.parking_slot import ParkingSlot


def branch_and_bound_allocate(
    slots: list[ParkingSlot],
    required_slots: int,
) -> list[ParkingSlot]:
    available_slots = [slot for slot in slots if slot.is_available()]

    if required_slots <= 0:
        return []

    if len(available_slots) < required_slots:
        return []

    # Sort by distance so promising solutions are explored first.
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

        # Branch 1: choose the current slot.
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

        # Branch 2: skip the current slot.
        search(
            index + 1,
            selected,
            current_cost,
        )

    search(0, [], 0.0)

    return best_solution
