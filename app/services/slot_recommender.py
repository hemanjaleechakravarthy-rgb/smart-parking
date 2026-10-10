
from app.models.parking_slot import ParkingSlot


def recommend_slots(
    slots: list[ParkingSlot],
    vehicle_type: str = "car",
    priority_required: bool = False,
    ev_charging_required: bool = False,
) -> list[dict]:
    """Rank eligible parking slots using a simple score."""

    eligible = [
        slot for slot in slots
        if slot.is_available()
        and slot.vehicle_type == vehicle_type
        and (not priority_required or slot.priority)
        and (not ev_charging_required or slot.ev_charging)
    ]

    if not eligible:
        return []

    max_distance = max(
        (slot.distance_from_entrance for slot in eligible),
        default=1,
    )
    max_distance = max(max_distance, 1)

    results = []

    for slot in eligible:
        score = 100 * (
            1 - slot.distance_from_entrance / max_distance
        )

        reasons = [
            f"{slot.distance_from_entrance} m from entrance"
        ]

        if slot.priority:
            score += 10
            reasons.append("priority slot")

        if slot.ev_charging:
            score += 10
            reasons.append("EV charging available")

        score = min(round(score, 2), 100)

        results.append({
            "Slot": slot.slot_id,
            "Vehicle Type": slot.vehicle_type,
            "Distance (m)": slot.distance_from_entrance,
            "Score": score,
            "Reason": ", ".join(reasons),
        })

    return sorted(
        results,
        key=lambda item: item["Score"],
        reverse=True,
    )
