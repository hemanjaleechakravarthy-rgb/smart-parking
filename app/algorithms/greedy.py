from app.models.parking_lot import ParkingLot
from app.models.parking_slot import ParkingSlot
from app.models.vehicle import Vehicle


def greedy_allocate(lot: ParkingLot, vehicle: Vehicle) -> ParkingSlot | None:
    suitable_slots = [
        slot
        for slot in lot.available_slots()
        if slot.vehicle_type == vehicle.vehicle_type
    ]

    if not suitable_slots:
        return None

    selected_slot = min(suitable_slots, key=lambda slot: slot.distance_from_entrance)

    selected_slot.occupy()
    return selected_slot
