
from streamlit.testing.v1 import AppTest


def test_streamlit_parking_allocation_e2e() -> None:
    app = AppTest.from_file("../streamlit_app.py")
    app.run(timeout=10)

    assert not app.exception

    app.sidebar.selectbox[0].set_value("Greedy")
    app.sidebar.text_input[0].set_value("AP39AB1234")
    app.run(timeout=10)

    # Generate algorithm-based suggestions.
    app.button[0].click()
    app.run(timeout=10)

    assert not app.exception
    assert len(app.radio) > 0

    # Choose a suggested slot.
    app.radio[0].set_value("P02")
    app.run(timeout=10)

    # Confirm the selected slot.
    confirm_button = next(
        button for button in app.button
        if button.label == "Confirm Selected Slot"
    )
    confirm_button.click()
    app.run(timeout=10)

    assert not app.exception
    print("SUCCESS MESSAGES:", [s.value for s in app.success])
    print("ERROR MESSAGES:", [e.value for e in app.error])
    print("EXCEPTIONS:", [e.message for e in app.exception])
    assert not app.exception