import streamlit as st

from app.algorithms.backtracking import backtracking_allocate
from app.algorithms.branch_bound import branch_and_bound_allocate
from app.algorithms.divide_conquer import find_nearest_slot
from app.algorithms.dynamic_programming import optimal_slot_allocation
from app.algorithms.greedy import greedy_allocate
from app.models.parking_lot import ParkingLot
from app.models.parking_slot import ParkingSlot
from app.models.vehicle import Vehicle


def create_lot() -> ParkingLot:
    lot = ParkingLot()

    lot.add_slot(ParkingSlot("P01", 30.0))
    lot.add_slot(ParkingSlot("P02", 10.0))
    lot.add_slot(ParkingSlot("P03", 20.0))
    lot.add_slot(ParkingSlot("P04", 40.0))
    lot.add_slot(ParkingSlot("P05", 15.0))
    lot.add_slot(ParkingSlot("P06", 50.0))

    return lot


st.set_page_config(
    page_title="Smart Parking",
    page_icon="🚗",
    layout="wide",
)

st.title("🚗 Smart Parking Space Management System")
st.write(
    "Algorithm-based parking slot allocation using Python."
)

st.sidebar.header("Parking Configuration")

algorithm = st.sidebar.selectbox(
    "Select Algorithm",
    [
        "Greedy",
        "Divide & Conquer",
        "Dynamic Programming",
        "Backtracking",
        "Branch & Bound",
    ],
)

required_slots = st.sidebar.number_input(
    "Number of Slots",
    min_value=1,
    max_value=6,
    value=1,
)

vehicle_number = st.sidebar.text_input(
    "Vehicle Number",
    value="AP39AB1234",
)

if st.button("Allocate Parking Slot"):
    lot = create_lot()

    vehicle = Vehicle(
        vehicle_number=vehicle_number,
        vehicle_type="car",
    )

    selected_slots = []

    if algorithm == "Greedy":
        slot = greedy_allocate(lot, vehicle)
        if slot:
            selected_slots = [slot]

    elif algorithm == "Divide & Conquer":
        slot = find_nearest_slot(lot.slots)
        if slot:
            selected_slots = [slot]

    elif algorithm == "Dynamic Programming":
        selected_slots = optimal_slot_allocation(
            lot.slots,
            required_slots,
        )

    elif algorithm == "Backtracking":
        selected_slots = backtracking_allocate(
            lot.slots,
            required_slots,
        )

    elif algorithm == "Branch & Bound":
        selected_slots = branch_and_bound_allocate(
            lot.slots,
            required_slots,
        )

    if selected_slots:
        st.success(
            f"Allocation successful using {algorithm}!"
        )

        st.subheader("Allocated Slots")

        for slot in selected_slots:
            st.info(
                f"🅿️ {slot.slot_id} — "
                f"{slot.distance_from_entrance} m from entrance"
            )

    else:
        st.error("No suitable parking slot available.")

st.divider()

st.subheader("Parking Lot Status")

lot = create_lot()

columns = st.columns(3)

for index, slot in enumerate(lot.slots):
    with columns[index % 3]:
        st.metric(
            label=f"🅿️ {slot.slot_id}",
            value="AVAILABLE" if slot.is_available() else "OCCUPIED",
            delta=f"{slot.distance_from_entrance} m",
        )

st.divider()

st.caption(
    "Smart Parking Space Management System | "
    "Computational Thinking & Programming Project"
)