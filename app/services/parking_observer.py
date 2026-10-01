from abc import ABC, abstractmethod


class ParkingObserver(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass


class ParkingDisplay(ParkingObserver):
    def update(self, message: str) -> None:
        print(f"DISPLAY: {message}")


class ParkingLogger(ParkingObserver):
    def update(self, message: str) -> None:
        print(f"LOG: {message}")


class ParkingEventManager:
    def __init__(self) -> None:
        self.observers: list[ParkingObserver] = []

    def add_observer(self, observer: ParkingObserver) -> None:
        self.observers.append(observer)

    def notify(self, message: str) -> None:
        for observer in self.observers:
            observer.update(message)
