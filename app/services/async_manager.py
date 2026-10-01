import asyncio

from app.models.parking_slot import ParkingSlot


async def check_slot_async(
    slot: ParkingSlot,
) -> tuple[str, bool]:
    await asyncio.sleep(0)
    return slot.slot_id, slot.is_available()


async def check_slots_async(
    slots: list[ParkingSlot],
) -> list[tuple[str, bool]]:
    tasks = [check_slot_async(slot) for slot in slots]

    return await asyncio.gather(*tasks)
