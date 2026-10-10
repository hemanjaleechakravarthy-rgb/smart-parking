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

from app.services.slot_recommender import recommend_slots





# =========================================================

# CREATE PARKING LOT

# =========================================================





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





# =========================================================

# RUN SELECTED ALGORITHM

# =========================================================





def run_algorithm(

    algorithm: str,

    lot: ParkingLot,

    vehicle: Vehicle,

    priority_required: bool,

    ev_charging_required: bool,

):

    """

    Run the selected parking algorithm for one vehicle.

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



def get_algorithm_candidates(

    algorithm: str,

    lot: ParkingLot,

    vehicle: Vehicle,

    priority_required: bool,

    ev_charging_required: bool,

) -> list[ParkingSlot]:

    """Return suitable candidate slots without occupying them."""



    candidates = [

        slot

        for slot in lot.slots

        if slot.is_available()

        and slot.vehicle_type == vehicle.vehicle_type

        and (not priority_required or slot.priority)

        and (not ev_charging_required or slot.ev_charging)

    ]



    if algorithm == "Greedy":

        return sorted(

            candidates,

            key=lambda slot: slot.distance_from_entrance,

        )



    if algorithm == "Divide & Conquer":

        result = find_nearest_slot(

            candidates,

            len(candidates),

            vehicle.vehicle_type,

            priority_required,

            ev_charging_required,

        )

        return result if isinstance(result, list) else (

            [result] if result else []

        )



    if algorithm == "Dynamic Programming":

        return optimal_slot_allocation(

            candidates,

            min(3, len(candidates)),

            vehicle.vehicle_type,

            priority_required,

            ev_charging_required,

        ) if candidates else []



    if algorithm == "Backtracking":

        return backtracking_allocate(

            candidates,

            min(3, len(candidates)),

            vehicle.vehicle_type,

            priority_required,

            ev_charging_required,

        ) if candidates else []



    if algorithm == "Branch & Bound":

        return branch_and_bound_allocate(

            candidates,

            min(3, len(candidates)),

            vehicle.vehicle_type,

            priority_required,

            ev_charging_required,

        ) if candidates else []



    return []

# =========================================================

# STREAMLIT CONFIGURATION

# =========================================================



st.set_page_config(

    page_title="Smart Parking",

    page_icon="🚗",

    layout="wide",

)





# =========================================================

# SMART PARKING UI STYLING

# =========================================================



st.markdown(

    """

    <style>



    /* =====================================================

       GLOBAL APPLICATION

       ===================================================== */



    .stApp {

        background:

            radial-gradient(

                circle at top right,

                rgba(37, 99, 235, 0.16),

                transparent 35%

            ),

            linear-gradient(

                135deg,

                #07111f 0%,

                #0b1728 50%,

                #0f1d31 100%

            );

    }



    .block-container {

        max-width: 1400px;

        padding-top: 3rem !important;

        padding-bottom: 3rem !important;

    }





    /* =====================================================

       STREAMLIT HEADER

       ===================================================== */



    header[data-testid="stHeader"] {

        background: rgba(7, 17, 31, 0.96) !important;

        border-bottom: 1px solid rgba(148, 163, 184, 0.12);

    }





    /* =====================================================

       GLOBAL TEXT

       ===================================================== */



    .stMarkdown,

    .stMarkdown p,

    .stMarkdown span,

    .stMarkdown div {

        color: #e5e7eb;

    }



    label,

    [data-testid="stWidgetLabel"],

    [data-testid="stWidgetLabel"] p {

        color: #cbd5e1 !important;

    }



    h1,

    h2,

    h3,

    h4 {

        color: #f8fafc !important;

    }





    /* =====================================================

       MAIN TITLE

       ===================================================== */



    .main-title {

        font-size: 44px;

        font-weight: 800;

        letter-spacing: 1px;

        color: #f8fafc !important;

        margin-bottom: 2px;

    }



    .main-subtitle {

        font-size: 17px;

        color: #94a3b8 !important;

        margin-bottom: 16px;

    }



    .system-status {

        display: inline-flex;

        align-items: center;

        gap: 8px;

        padding: 7px 14px;

        border-radius: 20px;

        background: rgba(34, 197, 94, 0.10);

        border: 1px solid rgba(34, 197, 94, 0.35);

        color: #86efac !important;

        font-size: 13px;

        font-weight: 700;

        letter-spacing: 0.5px;

    }



    .status-dot {

        width: 8px;

        height: 8px;

        border-radius: 50%;

        background: #22c55e;

        box-shadow: 0 0 10px rgba(34, 197, 94, 0.8);

    }





    /* =====================================================

       METRICS

       ===================================================== */



    [data-testid="stMetricLabel"] {

        color: #94a3b8 !important;

    }



    [data-testid="stMetricValue"] {

        color: #f8fafc !important;

        font-weight: 800;

    }



    [data-testid="stMetricDelta"] {

        color: #94a3b8 !important;

    }





    /* =====================================================

       SIDEBAR

       ===================================================== */



    section[data-testid="stSidebar"] {

        background:

            linear-gradient(

                180deg,

                #070e1b 0%,

                #0b1424 100%

            );

        border-right: 1px solid rgba(148, 163, 184, 0.12);

    }



    section[data-testid="stSidebar"] * {

        color: #e5e7eb;

    }





    /* =====================================================

       DROPDOWN / SELECTBOX VISIBILITY

       ===================================================== */



    section[data-testid="stSidebar"] div[data-baseweb="select"] {

        color: #111827 !important;

    }



    section[data-testid="stSidebar"]

    div[data-baseweb="select"] > div {

        background-color: #f8fafc !important;

        color: #111827 !important;

        border-radius: 8px !important;

    }



    section[data-testid="stSidebar"]

    div[data-baseweb="select"] span {

        color: #111827 !important;

    }



    section[data-testid="stSidebar"]

    div[data-baseweb="select"] input {

        color: #111827 !important;

    }



    div[data-baseweb="popover"] {

        background-color: #f8fafc !important;

    }



    div[data-baseweb="popover"] li {

        color: #111827 !important;

    }



    div[data-baseweb="popover"] li:hover {

        background-color: #e5e7eb !important;

    }





    /* =====================================================

       TEXT INPUT VISIBILITY

       ===================================================== */



    input,

    textarea {

        color: #111827 !important;

        background-color: #f8fafc !important;

    }



    section[data-testid="stSidebar"]

    input {

        color: #111827 !important;

        background-color: #f8fafc !important;

    }





    /* =====================================================

       BUTTONS

       ===================================================== */



    .stButton > button {

        border-radius: 10px;

        font-weight: 800 !important;

        color: #111827 !important;

        background-color: #f8fafc !important;

        border: 1px solid rgba(96, 165, 250, 0.45);

        transition: all 0.2s ease;

    }



    .stButton > button p {

        color: #111827 !important;

        font-weight: 800 !important;

    }



    .stButton > button:hover {

        transform: translateY(-2px);

        border-color: #60a5fa;

        box-shadow:

            0 6px 18px rgba(59, 130, 246, 0.25);

    }





    /* =====================================================

       DATAFRAME / BENCHMARK TABLE

       ===================================================== */



    [data-testid="stDataFrame"] {

        border-radius: 12px;

        overflow: hidden;

    }



    [data-testid="stDataFrame"] * {

        color: #111827 !important;

    }



    [data-testid="stDataFrame"] th {

        color: #111827 !important;

        font-weight: 800 !important;

    }





    /* =====================================================

       TABLE

       ===================================================== */



    table {

        color: #111827 !important;

    }



    thead th {

        color: #111827 !important;

        font-weight: 800 !important;

    }



    tbody td {

        color: #111827 !important;

    }





    /* =====================================================

       SECTION SPACING

       ===================================================== */



    hr {

        border-color: rgba(148, 163, 184, 0.12);

        margin-top: 30px;

        margin-bottom: 30px;

    }



    </style>

    """,

    unsafe_allow_html=True,

)





# =========================================================

# HEADER

# =========================================================



st.title("🅿️ Smart Parking")
st.subheader("Intelligent Space Allocation & Management System")
st.success("🟢 SYSTEM ONLINE")

st.write("Algorithm-based parking slot allocation using Python.")





# =========================================================

# SIDEBAR

# =========================================================



st.sidebar.header("🚗 Parking Configuration")





# =========================================================

# PARKING CONFIGURATION

# =========================================================



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





# =========================================================

# VEHICLE CONFIGURATION

# =========================================================



vehicle_configs = []





if required_slots == 1:

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





# =========================================================

# SESSION STATE

# =========================================================



if "parking_lot" not in st.session_state:

    st.session_state.parking_lot = create_lot()



if "parked_vehicles" not in st.session_state:

    st.session_state.parked_vehicles = {}



if "selected_slots" not in st.session_state:

    st.session_state.selected_slots = []





lot = st.session_state.parking_lot





# =========================================================

# LIVE PARKING STATISTICS

# =========================================================



total_slots = lot.total_slots()

available_slots = lot.available_count()

occupied_slots = total_slots - available_slots



occupancy_percentage = (occupied_slots / total_slots) * 100 if total_slots > 0 else 0





st.subheader("📊 Parking Statistics")



col1, col2, col3, col4 = st.columns(4)





with col1:

    st.metric(

        "TOTAL SLOTS",

        total_slots,

    )





with col2:

    st.metric(

        "AVAILABLE",

        available_slots,

    )





with col3:

    st.metric(

        "OCCUPIED",

        occupied_slots,

    )





with col4:

    st.metric(

        "OCCUPANCY",

        f"{occupancy_percentage:.1f}%",

    )





# =========================================================
# ALGORITHM-BASED SUGGESTIONS AND USER CONFIRMATION
# =========================================================

if st.session_state.get("last_allocation_message"):
    st.success(st.session_state.last_allocation_message)
    st.session_state.last_allocation_message = None

st.subheader("🧠 Algorithm-Based Parking Suggestions")
st.caption(
    "Find suggestions using the selected algorithm, choose a slot "
    "for each vehicle, and confirm before occupying any slots."
)

if st.button("Find Parking Suggestions", key="find_suggestions"):
    suggestions_by_vehicle = {}

    for index, config in enumerate(vehicle_configs):
        vehicle = Vehicle(
            config["vehicle_number"],
            config["vehicle_type"],
            priority=2 if config["priority"] else 1,
        )
        candidates = get_algorithm_candidates(
            algorithm,
            lot,
            vehicle,
            config["priority"],
            config["ev_charging"],
        )
        suggestions_by_vehicle[str(index)] = [
            slot.slot_id for slot in candidates
        ]

    st.session_state.pending_slot_choice = {
        "algorithm": algorithm,
        "configs": [dict(config) for config in vehicle_configs],
        "suggestions": suggestions_by_vehicle,
    }

pending = st.session_state.get("pending_slot_choice")

if pending:
    current_configs = [dict(config) for config in vehicle_configs]
    if (
        pending["algorithm"] != algorithm
        or pending["configs"] != current_configs
    ):
        st.session_state.pending_slot_choice = None
        st.info("Your settings changed. Find parking suggestions again.")
    else:
        slots_by_id = {slot.slot_id: slot for slot in lot.slots}
        choices = {}
        unavailable_vehicle = False

        # Show algorithm-generated suggestions for each vehicle.
        for index, config in enumerate(vehicle_configs):
            vehicle_number = config["vehicle_number"]
            st.markdown(
                f"**Vehicle {index + 1}: {vehicle_number} "
                f"({config['vehicle_type']})**"
            )
            candidate_ids = pending["suggestions"].get(str(index), [])
            candidates = [
                slots_by_id[slot_id]
                for slot_id in candidate_ids
                if slot_id in slots_by_id
                and slots_by_id[slot_id].is_available()
                and slots_by_id[slot_id].vehicle_type == config["vehicle_type"]
                and (not config["priority"] or slots_by_id[slot_id].priority)
                and (
                    not config["ev_charging"]
                    or slots_by_id[slot_id].ev_charging
                )
            ]

            if not candidates:
                st.warning(
                    f"No suggested slots are available for {vehicle_number}. "
                    "Find suggestions again."
                )
                unavailable_vehicle = True
                continue

            st.dataframe(
                [
                    {
                        "Slot": slot.slot_id,
                        "Distance (m)": slot.distance_from_entrance,
                        "Priority": slot.priority,
                        "EV Charging": slot.ev_charging,
                    }
                    for slot in candidates
                ],
                hide_index=True,
                width="stretch",
            )
            choices[index] = st.radio(
                f"Choose a slot for {vehicle_number}",
                options=[slot.slot_id for slot in candidates],
                format_func=lambda slot_id: (
                    f"{slot_id} — "
                    f"{slots_by_id[slot_id].distance_from_entrance} m "
                    "from entrance"
                ),
                key=f"chosen_slot_{index}",
            )

        # Confirm all selected slots together, before occupying any of them.
        if not unavailable_vehicle and len(choices) == len(vehicle_configs):
            confirm_label = (
                "Confirm Selected Slot"
                if len(vehicle_configs) == 1
                else "Confirm All Selected Slots"
            )
            if st.button(confirm_label, key="confirm_all_selected_slots"):
                selected_ids = list(choices.values())
                if len(set(selected_ids)) != len(selected_ids):
                    st.error(
                        "Each vehicle must have a different parking slot. "
                        "Please change your selections."
                    )
                elif any(
                    config["vehicle_number"]
                    in st.session_state.parked_vehicles
                    for config in vehicle_configs
                ):
                    st.error(
                        "At least one vehicle is already parked. "
                        "Check the vehicle numbers."
                    )
                else:
                    selected_slots = [
                        slots_by_id[slot_id] for slot_id in selected_ids
                    ]
                    valid = all(
                        slot.is_available()
                        and slot.vehicle_type == config["vehicle_type"]
                        and (not config["priority"] or slot.priority)
                        and (
                            not config["ev_charging"]
                            or slot.ev_charging
                        )
                        for slot, config in zip(selected_slots, vehicle_configs)
                    )
                    if not valid:
                        st.error(
                            "A selected slot is no longer suitable or "
                            "available. Find suggestions again."
                        )
                        st.session_state.pending_slot_choice = None
                    else:
                        for slot, config in zip(selected_slots, vehicle_configs):
                            slot.occupy()
                            st.session_state.parked_vehicles[
                                config["vehicle_number"]
                            ] = [slot.slot_id]
                        st.session_state.selected_slots = [
                            *st.session_state.selected_slots,
                            *selected_slots,
                        ]
                        st.session_state.last_allocation_message = (
                            f"Allocation successful using {algorithm}!"
                        )
                        st.session_state.pending_slot_choice = None
                        st.rerun()

# =========================================================

# RELEASE VEHICLE

# =========================================================



st.subheader("🚪 Release Vehicle")



release_vehicle = st.text_input(

    "Enter Vehicle Number to Release",

    key="release_vehicle",

)





if st.button("Release Vehicle"):

    if release_vehicle in st.session_state.parked_vehicles:

        slot_ids = st.session_state.parked_vehicles.pop(release_vehicle)



        for slot in lot.slots:

            if slot.slot_id in slot_ids:

                slot.release()



        st.session_state.selected_slots = [

            slot

            for slot in st.session_state.selected_slots

            if slot.slot_id not in slot_ids

        ]



        st.success(f"Vehicle {release_vehicle} released from {', '.join(slot_ids)}.")



    else:

        st.error("Vehicle not found in the parking lot.")





# =========================================================

# PARKING LOT DISPLAY

# =========================================================



st.divider()



st.subheader("🅿️ Parking Lot")



st.write("🚪 Entrance")



columns = st.columns(3)





for index, slot in enumerate(lot.slots):

    with columns[index % 3]:

        with st.container(border=True, height=260):

            st.markdown(f"### 🅿️ {slot.slot_id}")



            if slot.is_available():

                st.success("🟢 AVAILABLE")



            else:

                st.error("🔴 OCCUPIED")



            st.write(f"🚗 **Type:** {slot.vehicle_type}")



            st.write(f"📏 **Distance:** {slot.distance_from_entrance} m")



            if slot.ev_charging:

                st.write("⚡ **EV Charging Available**")



            if slot.priority:

                st.write("⭐ **Priority Slot**")





st.caption("🟢 Available   🔴 Occupied   ⭐ Priority   ⚡ EV Charging")





# =========================================================

# ALGORITHM PERFORMANCE COMPARISON

# =========================================================



st.divider()



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



    # -----------------------------------------------------

    # BENCHMARK TABLE

    # -----------------------------------------------------



    st.dataframe(

        display_rows,

        width="stretch",

        hide_index=True,

    )



    
    # -----------------------------------------------------
    # EXECUTION TIME TREND
    # -----------------------------------------------------

    st.markdown("### 📈 Execution Time vs Parking Lot Size")

    st.write(
        "Compare the execution time of faster algorithms "
        "separately from Backtracking to make both trends "
        "easier to read."
    )

    # Chart 1: Faster algorithms
    st.markdown("#### ⚡ Faster Algorithms")

    fast_chart_data = {
        "Parking Slots": [row["Parking Slots"] for row in display_rows],
        "Greedy": [row["Greedy"] for row in display_rows],
        "Divide & Conquer": [
            row["Divide & Conquer"] for row in display_rows
        ],
        "Dynamic Programming": [
            row["Dynamic Programming"] for row in display_rows
        ],
        "Branch & Bound": [
            row["Branch & Bound"] for row in display_rows
        ],
    }

    st.line_chart(
        fast_chart_data,
        x="Parking Slots",
        y=[
            "Greedy",
            "Divide & Conquer",
            "Dynamic Programming",
            "Branch & Bound",
        ],
        width="stretch",
    )

    # Chart 2: Backtracking
    st.markdown("#### 🔍 Backtracking")

    backtracking_chart_data = {
        "Parking Slots": [row["Parking Slots"] for row in display_rows],
        "Backtracking": [row["Backtracking"] for row in display_rows],
    }

    st.line_chart(
        backtracking_chart_data,
        x="Parking Slots",
        y=["Backtracking"],
        width="stretch",
    )

    st.caption(
        "Lower execution time indicates faster performance. "
        "Results are based on the benchmark measurements "
        "stored in benchmarks/results.csv."
    )
    if display_rows:
        largest_lot = max(
            display_rows,
            key=lambda row: row["Parking Slots"]
        )

        algorithm_names = [
            "Greedy",
            "Divide & Conquer",
            "Dynamic Programming",
            "Backtracking",
            "Branch & Bound",
        ]

        fastest_algorithm = min(
            algorithm_names,
            key=lambda name: largest_lot[name]
        )

        st.success(
            f"Fastest algorithm for {largest_lot['Parking Slots']} "
            f"parking slots: {fastest_algorithm} "
            f"({largest_lot[fastest_algorithm]:.4f} seconds)"
        )

except FileNotFoundError:
    st.error("Benchmark file not found: benchmarks/results.csv")
except (KeyError, ValueError) as error:
    st.error(f"Invalid benchmark CSV data: {error}")
# =========================================================

# FOOTER

# =========================================================



st.divider()



st.caption(

    "Smart Parking Space Management System | "

    "Computational Thinking & Programming Project"

)
