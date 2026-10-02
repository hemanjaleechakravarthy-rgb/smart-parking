from streamlit.testing.v1 import AppTest


def test_streamlit_parking_allocation_e2e() -> None:
    app = AppTest.from_file("../streamlit_app.py")

    app.run()

    assert not app.exception

    app.sidebar.selectbox[0].set_value("Greedy")
    app.sidebar.text_input[0].set_value("AP39AB1234")
    app.button[0].click()

    app.run()

    assert not app.exception
    assert len(app.success) > 0
    assert "Allocation successful" in app.success[0].value
