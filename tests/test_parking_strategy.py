from app.models.parking_slot import ParkingSlot
from app.services.parking_strategy import NearestSlotStrategy


def test_nearest_slot_strategy() -> None:
    slots = [
        ParkingSlot("P01", 30.0),
        ParkingSlot("P02", 10.0),
        ParkingSlot("P03", 20.0),
    ]

    strategy = NearestSlotStrategy()
    result = strategy.allocate(slots, 2)

    assert [slot.slot_id for slot in result] == ["P02", "P03"]


from app.services.parking_strategy_factory import ParkingStrategyFactory


def test_strategy_factory_creates_nearest_strategy() -> None:
    strategy = ParkingStrategyFactory.create("nearest")

    assert isinstance(strategy, NearestSlotStrategy)


def test_strategy_factory_rejects_unknown_strategy() -> None:
    try:
        ParkingStrategyFactory.create("unknown")
        assert False
    except ValueError:
        assert True


def test_parking_strategy_base_method() -> None:
    from app.services.parking_strategy import ParkingStrategy

    class ConcreteStrategy(ParkingStrategy):
        def allocate(self, slots, required_slots):
            return super().allocate(slots, required_slots)

    strategy = ConcreteStrategy()
    result = strategy.allocate([], 1)

    assert result is None
