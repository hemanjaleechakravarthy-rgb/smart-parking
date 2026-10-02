from app.services.parking_strategy import (
    NearestSlotStrategy,
    ParkingStrategy,
)


class ParkingStrategyFactory:
    """Factory for creating parking allocation strategies."""

    @staticmethod
    def create(strategy_name: str) -> ParkingStrategy:
        if strategy_name.lower() == "nearest":
            return NearestSlotStrategy()

        raise ValueError(f"Unknown parking strategy: {strategy_name}")
