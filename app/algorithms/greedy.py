from app.models.parking_lot import ParkingLot
from app.models.parking_slot import ParkingSlot
from app.models.vehicle import Vehicle


def greedy_allocate(
    lot: ParkingLot,
    vehicle: Vehicle,
    required_slots: int = 1,
    priority_required: bool = False,
    ev_charging_required: bool = False,
) -> ParkingSlot | list[ParkingSlot] | None:
    """
    Allocate parking slots using the Greedy algorithm.
    """

    selected_slots: list[ParkingSlot] = []

    for _ in range(required_slots):
        suitable_slots = [
            slot
            for slot in lot.available_slots()
            if slot.vehicle_type == vehicle.vehicle_type
            and (not priority_required or slot.priority)
            and (not ev_charging_required or slot.ev_charging)
        ]

        if not suitable_slots:
            break

        selected_slot = min(
            suitable_slots,
            key=lambda slot: slot.distance_from_entrance,
        )

        selected_slot.occupy()
        selected_slots.append(selected_slot)

    if not selected_slots:
        return None

    if required_slots == 1:
        return selected_slots[0]

    return selected_slots
