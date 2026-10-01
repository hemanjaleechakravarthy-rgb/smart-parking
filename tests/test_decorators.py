from app.utils.decorators import log_operation


def test_log_operation_decorator(capsys) -> None:
    @log_operation
    def sample_operation() -> str:
        return "success"

    result = sample_operation()

    captured = capsys.readouterr()

    assert result == "success"
    assert "Starting: sample_operation" in captured.out
    assert "Completed: sample_operation" in captured.out
