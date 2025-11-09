import sys
import os
import json

from cars.Car import Car, write_cars_to_file

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))


def test_write_cars_to_file(tmp_path):
    cars = [
        Car("BMW", "X5", 12.3, ["leather", "heated seats", "GPS"]),
        Car("Audi", "A6", 9.93, ["leather", "heated seats", "panorama", "GPS"]),
    ]

    file_path = tmp_path / "cars_test.json"
    write_cars_to_file(cars, str(file_path))

    # Verify file exists
    assert os.path.exists(file_path)

    # Verify file content is valid JSON and matches the cars written
    with open(file_path, "r") as f:
        data = json.load(f)

    # Expect list of dicts with car properties
    assert isinstance(data, list)
    assert len(data) == 2

    for car_dict, car in zip(data, cars):
        assert car_dict["make"] == car.make
        assert car_dict["model"] == car.model
        assert car_dict["fuel_consumption"] == car.fuel_consumption
        assert car_dict["features"] == car.features
