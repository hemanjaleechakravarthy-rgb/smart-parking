from app.models.parking_slot import ParkingSlot


def optimal_slot_allocation(
    slots: list[ParkingSlot],
    required_slots: int,
) -> list[ParkingSlot]:
    available_slots = [slot for slot in slots if slot.is_available()]

    if required_slots <= 0:
        return []

    if required_slots > len(available_slots):
        return []

    n = len(available_slots)

    # dp[i][j] = minimum total distance when selecting
    # exactly j slots from the first i available slots.
    dp: list[list[float]] = [
        [float("inf")] * (required_slots + 1) for _ in range(n + 1)
    ]

    # Selecting zero slots has zero cost.
    for i in range(n + 1):
        dp[i][0] = 0.0

    for i in range(1, n + 1):
        distance = available_slots[i - 1].distance_from_entrance

        for j in range(1, min(i, required_slots) + 1):
            without_current = dp[i - 1][j]
            with_current = dp[i - 1][j - 1] + distance

            dp[i][j] = min(
                without_current,
                with_current,
            )

    # Backtrack through the DP table to recover the selected slots.
    selected: list[ParkingSlot] = []
    i = n
    j = required_slots

    while j > 0:
        current_distance = available_slots[i - 1].distance_from_entrance

        if dp[i][j] == dp[i - 1][j - 1] + current_distance:
            selected.append(available_slots[i - 1])
            j -= 1

        i -= 1

    selected.reverse()

    return selected
