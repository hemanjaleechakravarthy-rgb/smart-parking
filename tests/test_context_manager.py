from app.utils.context_manager import parking_operation


def test_parking_operation_context_manager(capsys) -> None:
    with parking_operation("Test Allocation"):
        print("Allocating slot")

    captured = capsys.readouterr()

    assert "Starting operation: Test Allocation" in captured.out
    assert "Allocating slot" in captured.out
    assert "Finished operation: Test Allocation" in captured.out
