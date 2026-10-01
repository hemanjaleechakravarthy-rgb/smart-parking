from app.services.parking_observer import (
    ParkingDisplay,
    ParkingEventManager,
    ParkingLogger,
)


def test_observer_notification() -> None:
    manager = ParkingEventManager()

    display = ParkingDisplay()
    logger = ParkingLogger()

    manager.add_observer(display)
    manager.add_observer(logger)

    manager.notify("Slot P01 occupied")

    assert len(manager.observers) == 2


def test_parking_observer_base_update() -> None:
    from app.services.parking_observer import ParkingObserver

    class TestObserver(ParkingObserver):
        def update(self, message: str) -> None:
            pass

    observer = TestObserver()

    observer.update("Test parking event")

    assert isinstance(observer, ParkingObserver)
