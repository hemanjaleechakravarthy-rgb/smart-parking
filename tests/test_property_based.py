from hypothesis import given
from hypothesis import strategies as st

from app.models.parking_slot import ParkingSlot


@given(
    slot_id=st.text(min_size=1, max_size=10),
    distance=st.floats(
        min_value=0,
        max_value=1000,
        allow_nan=False,
        allow_infinity=False,
    ),
)
def test_new_slot_is_always_available(
    slot_id: str,
    distance: float,
) -> None:
    slot = ParkingSlot(
        slot_id=slot_id,
        distance_from_entrance=distance,
    )

    assert slot.is_available() is True
