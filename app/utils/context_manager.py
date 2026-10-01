from collections.abc import Iterator
from contextlib import contextmanager


@contextmanager
def parking_operation(operation_name: str) -> Iterator[None]:
    print(f"Starting operation: {operation_name}")

    try:
        yield
    finally:
        print(f"Finished operation: {operation_name}")
