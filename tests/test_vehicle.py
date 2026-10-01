from app.models.vehicle import Bike, Car, ElectricVehicle


def test_vehicle_types() -> None:
    car = Car("AP39AB1234")
    bike = Bike("AP39CD5678")
    ev = ElectricVehicle("AP39EF9012")

    assert car.vehicle_type == "car"
    assert bike.vehicle_type == "bike"
    assert ev.vehicle_type == "ev"


def test_priority_vehicle() -> None:
    from app.models.vehicle import Vehicle

    vehicle = Vehicle(
        vehicle_number="AP39PR1234",
        vehicle_type="car",
        priority=2,
    )

    assert vehicle.is_priority_vehicle() is True
