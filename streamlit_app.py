import csv
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

    lot.add_slot(
        ParkingSlot(
            "P01",
            30.0,
            "car",
            priority=False,
            ev_charging=False,
        )
    )

    lot.add_slot(
        ParkingSlot(
            "P02",
            10.0,
            "car",
            priority=True,
            ev_charging=False,
        )
    )

    lot.add_slot(
        ParkingSlot(
            "P03",
            20.0,
            "bike",
            priority=False,
            ev_charging=False,
        )
    )

    lot.add_slot(
        ParkingSlot(
            "P04",
            40.0,
            "car",
            priority=False,
            ev_charging=False,
        )
    )

    lot.add_slot(
        ParkingSlot(
            "P05",
            15.0,
            "ev",
            priority=True,
            ev_charging=True,
        )
    )

    lot.add_slot(
        ParkingSlot(
            "P06",
            50.0,
            "ev",
            priority=False,
            ev_charging=True,
        )
    )

    return lot


def run_algorithm(
    algorithm: str,
    lot: ParkingLot,
    vehicle: Vehicle,
    priority_required: bool,
    ev_charging_required: bool,
):
    """
    Run the selected parking algorithm for ONE vehicle.

    The existing algorithms are kept unchanged.
    """

    if algorithm == "Greedy":
        result = greedy_allocate(
            lot,
            vehicle,
            1,
            priority_required,
            ev_charging_required,
        )

        if result is None:
            return None

        if isinstance(result, list):
            return result[0] if result else None

        return result

    if algorithm == "Divide & Conquer":
        result = find_nearest_slot(
            lot.slots,
            1,
            vehicle.vehicle_type,
            priority_required,
            ev_charging_required,
        )

        if result is None:
            return None

        if isinstance(result, list):
            return result[0] if result else None

        return result

    if algorithm == "Dynamic Programming":
        result = optimal_slot_allocation(
            lot.slots,
            1,
            vehicle.vehicle_type,
            priority_required,
            ev_charging_required,
        )

        return result[0] if result else None

    if algorithm == "Backtracking":
        result = backtracking_allocate(
            lot.slots,
            1,
            vehicle.vehicle_type,
            priority_required,
            ev_charging_required,
        )

        return result[0] if result else None

    if algorithm == "Branch & Bound":
        result = branch_and_bound_allocate(
            lot.slots,
            1,
            vehicle.vehicle_type,
            priority_required,
            ev_charging_required,
        )

        return result[0] if result else None

    return None


st.set_page_config(
    page_title="Smart Parking",
    page_icon="🚗",
    layout="wide",
)

st.title("🚗 Smart Parking Space Management System")

st.write("Algorithm-based parking slot allocation using Python.")

st.sidebar.header("Parking Configuration")


# ---------------------------------------------------------
# PARKING CONFIGURATION
# ---------------------------------------------------------

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


# ---------------------------------------------------------
# VEHICLE CONFIGURATION
# ---------------------------------------------------------

vehicle_configs = []


if required_slots == 1:
    # Original single-vehicle functionality
    vehicle_number = st.sidebar.text_input(
        "Vehicle Number",
        value="AP39AB1234",
    )

    vehicle_type = st.sidebar.selectbox(
        "Vehicle Type",
        ["car", "bike", "ev"],
    )

    requires_priority = st.sidebar.checkbox(
        "⭐ Priority Parking",
    )

    requires_ev_charging = st.sidebar.checkbox(
        "⚡ EV Charging Required",
    )

    vehicle_configs.append(
        {
            "vehicle_number": vehicle_number,
            "vehicle_type": vehicle_type,
            "priority": requires_priority,
            "ev_charging": requires_ev_charging,
        }
    )

else:
    # -----------------------------------------------------
    # MULTI-VEHICLE CONFIGURATION
    # -----------------------------------------------------

    st.sidebar.subheader("🚗 Vehicle Details")

    for index in range(required_slots):
        st.sidebar.markdown(f"### Vehicle {index + 1}")

        vehicle_number = st.sidebar.text_input(
            f"Vehicle {index + 1} Number",
            value=f"AP39AB{1234 + index}",
            key=f"vehicle_number_{index}",
        )

        vehicle_type = st.sidebar.selectbox(
            f"Vehicle {index + 1} Type",
            ["car", "bike", "ev"],
            key=f"vehicle_type_{index}",
        )

        requires_priority = st.sidebar.checkbox(
            f"⭐ Vehicle {index + 1} Priority",
            key=f"priority_{index}",
        )

        requires_ev_charging = st.sidebar.checkbox(
            f"⚡ Vehicle {index + 1} EV Charging",
            key=f"ev_charging_{index}",
        )

        vehicle_configs.append(
            {
                "vehicle_number": vehicle_number,
                "vehicle_type": vehicle_type,
                "priority": requires_priority,
                "ev_charging": requires_ev_charging,
            }
        )


# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "parking_lot" not in st.session_state:
    st.session_state.parking_lot = create_lot()

if "parked_vehicles" not in st.session_state:
    st.session_state.parked_vehicles = {}

if "selected_slots" not in st.session_state:
    st.session_state.selected_slots = []


lot = st.session_state.parking_lot


# ---------------------------------------------------------
# LIVE PARKING STATISTICS
# ---------------------------------------------------------

total_slots = lot.total_slots()
available_slots = lot.available_count()
occupied_slots = total_slots - available_slots

occupancy_percentage = (occupied_slots / total_slots) * 100 if total_slots > 0 else 0

st.subheader("📊 Parking Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("TOTAL SLOTS", total_slots)

with col2:
    st.metric("AVAILABLE", available_slots)

with col3:
    st.metric("OCCUPIED", occupied_slots)

with col4:
    st.metric(
        "OCCUPANCY",
        f"{occupancy_percentage:.1f}%",
    )


# ---------------------------------------------------------
# ALLOCATE PARKING
# ---------------------------------------------------------

if st.button("Allocate Parking Slot"):
    allocated_slots = []
    allocation_details = []
    allocation_failed = False

    # -----------------------------------------------------
    # PROCESS EACH VEHICLE
    # -----------------------------------------------------

    for config in vehicle_configs:
        vehicle_number = config["vehicle_number"]
        vehicle_type = config["vehicle_type"]
        requires_priority = config["priority"]
        requires_ev_charging = config["ev_charging"]

        vehicle = Vehicle(
            vehicle_number,
            vehicle_type,
            priority=2 if requires_priority else 1,
        )

        selected_slot = run_algorithm(
            algorithm,
            lot,
            vehicle,
            requires_priority,
            requires_ev_charging,
        )

        # No suitable slot for this vehicle
        if selected_slot is None:
            allocation_failed = True

            st.error(
                f"Unable to allocate a slot for "
                f"{vehicle_number} ({vehicle_type}). "
                f"Not enough suitable slots are available."
            )

            break

        # -------------------------------------------------
        # Occupy selected slot
        # -------------------------------------------------

        if selected_slot.is_available():
            selected_slot.occupy()

        allocated_slots.append(selected_slot)

        allocation_details.append(
            {
                "vehicle_number": vehicle_number,
                "vehicle_type": vehicle_type,
                "slot": selected_slot,
                "priority": requires_priority,
                "ev_charging": requires_ev_charging,
            }
        )

    # -----------------------------------------------------
    # ROLLBACK IF ANY VEHICLE FAILED
    # -----------------------------------------------------

    if allocation_failed:
        for slot in allocated_slots:
            slot.release()

        st.session_state.selected_slots = []

    # -----------------------------------------------------
    # SUCCESSFUL ALLOCATION
    # -----------------------------------------------------

    else:
        st.session_state.selected_slots = allocated_slots

        # Store every vehicle separately.
        for details in allocation_details:
            vehicle_number = details["vehicle_number"]
            slot = details["slot"]

            st.session_state.parked_vehicles[vehicle_number] = [slot.slot_id]

        st.success(f"Allocation successful using {algorithm}!")

        # -------------------------------------------------
        # ALLOCATED SLOTS
        # -------------------------------------------------

        st.subheader("Allocated Slots")

        for details in allocation_details:
            vehicle_number = details["vehicle_number"]
            vehicle_type = details["vehicle_type"]
            slot = details["slot"]

            st.info(
                f"🚗 **{vehicle_number}** "
                f"({vehicle_type}) → "
                f"🅿️ **{slot.slot_id}** — "
                f"{slot.distance_from_entrance} m "
                f"from entrance"
            )

        # -------------------------------------------------
        # ALLOCATION SUMMARY
        # -------------------------------------------------

        slot_names = ", ".join(slot.slot_id for slot in allocated_slots)

        total_distance = sum(slot.distance_from_entrance for slot in allocated_slots)

        st.write(f"📌 **Allocated Slots:** {slot_names}")

        st.write(f"📏 **Total Distance:** {total_distance} m")

        # -------------------------------------------------
        # WHY THESE SLOTS?
        # -------------------------------------------------

        if algorithm == "Greedy":
            st.write(
                "💡 **Why these slots?** "
                "The Greedy algorithm selected the "
                "nearest suitable slot for each vehicle."
            )

        elif algorithm == "Divide & Conquer":
            st.write(
                "💡 **Why these slots?** "
                "The Divide & Conquer algorithm divided "
                "the suitable slots into smaller sections "
                "and selected the nearest suitable slot "
                "for each vehicle."
            )

        elif algorithm == "Dynamic Programming":
            st.write(
                "💡 **Why these slots?** "
                "Dynamic Programming selected the suitable "
                "slot that minimizes the distance for each "
                "vehicle."
            )

        elif algorithm == "Backtracking":
            st.write(
                "💡 **Why these slots?** "
                "Backtracking explored valid slot choices "
                "for each vehicle and selected a suitable "
                "minimum-distance slot."
            )

        elif algorithm == "Branch & Bound":
            st.write(
                "💡 **Why these slots?** "
                "Branch & Bound searched possible slot "
                "choices and pruned branches that could "
                "not improve the solution."
            )


# ---------------------------------------------------------
# RELEASE VEHICLE
# ---------------------------------------------------------

st.subheader("🚪 Release Vehicle")

release_vehicle = st.text_input(
    "Enter Vehicle Number to Release",
    key="release_vehicle",
)

if st.button("Release Vehicle"):
    if release_vehicle in st.session_state.parked_vehicles:
        # Get ALL slots assigned to this vehicle.
        slot_ids = st.session_state.parked_vehicles.pop(release_vehicle)

        # Release every slot.
        for slot in lot.slots:
            if slot.slot_id in slot_ids:
                slot.release()

        # Remove released slots from session state.
        st.session_state.selected_slots = [
            slot
            for slot in st.session_state.selected_slots
            if slot.slot_id not in slot_ids
        ]

        st.success(f"Vehicle {release_vehicle} released from {', '.join(slot_ids)}.")

    else:
        st.error("Vehicle not found in the parking lot.")


# ---------------------------------------------------------
# PARKING LOT DISPLAY
# ---------------------------------------------------------

st.divider()

st.subheader("🅿️ Parking Lot")

st.write("🚪 Entrance")

columns = st.columns(3)

for index, slot in enumerate(lot.slots):
    with columns[index % 3]:
        if slot.is_available():
            status = "🟢 AVAILABLE"
        else:
            status = "🔴 OCCUPIED"

        features = []

        if slot.priority:
            features.append("⭐ Priority")

        if slot.ev_charging:
            features.append("⚡ EV Charging")

        feature_text = " | ".join(features) if features else "Standard Slot"

        st.markdown(
            f"""
            ### 🅿️ {slot.slot_id}

            **{status}**

            🚗 Type: {slot.vehicle_type}

            📏 {slot.distance_from_entrance} m

            🔧 {feature_text}
            """
        )


st.caption("🟢 Available   🔴 Occupied   ⭐ Priority   ⚡ EV Charging")


# ---------------------------------------------------------
# ALGORITHM PERFORMANCE COMPARISON
# ---------------------------------------------------------

# ---------------------------------------------------------
# ALGORITHM PERFORMANCE COMPARISON
# ---------------------------------------------------------

st.subheader("⚡ Algorithm Performance Comparison")

try:
    with open(
        "benchmarks/results.csv",
        newline="",
        encoding="utf-8",
    ) as file:
        reader = csv.DictReader(file)
        benchmark_rows = list(reader)

    st.write("Benchmark execution time for different parking lot sizes.")

    display_rows = []

    for row in benchmark_rows:
        display_rows.append(
            {
                "Parking Slots": int(row["slots"]),
                "Greedy": float(row["greedy"]),
                "Divide & Conquer": float(row["divide_conquer"]),
                "Dynamic Programming": float(row["dynamic_programming"]),
                "Backtracking": float(row["backtracking"]),
                "Branch & Bound": float(row["branch_and_bound"]),
            }
        )

    st.dataframe(
        display_rows,
        width="stretch",
        hide_index=True,
    )

    st.markdown("### 📊 Average Execution Time")

    algorithms = [
        "greedy",
        "divide_conquer",
        "dynamic_programming",
        "backtracking",
        "branch_and_bound",
    ]

    average_times = {}

    for algorithm_name in algorithms:
        values = [float(row[algorithm_name]) for row in benchmark_rows]

        average_times[algorithm_name.replace("_", " ").title()] = sum(values) / len(
            values
        )

    st.bar_chart(
        average_times,
        width="stretch",
    )

    st.caption(
        "Average execution time across parking lot sizes of 5, 10, 15, 20 and 25 slots."
    )

except FileNotFoundError:
    st.warning("Benchmark results are not available. Run the benchmark first.")


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.divider()

st.caption(
    "Smart Parking Space Management System | "
    "Computational Thinking & Programming Project"
)
