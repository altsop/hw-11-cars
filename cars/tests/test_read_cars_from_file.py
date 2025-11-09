import sys
import os
import json
import pytest

from cars.Car import Car,  read_cars_from_file, write_cars_to_file

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

def test_read_cars_from_file(tmp_path):
    cars = [
        Car("BMW", "X5", 12.3, ["leather", "heated seats", "GPS"]),
        Car("Audi", "A6", 9.93, ["leather", "heated seats", "panorama", "GPS"]),
    ]

    file_path = tmp_path / "cars_test.json"
    # Write cars to file using the write function to ensure consistent format
    write_cars_to_file(cars, str(file_path))

    # Read them back using the read function
    read_cars = read_cars_from_file(str(file_path))

    assert len(read_cars) == len(cars)
    for original, read_back in zip(cars, read_cars):
        assert original == read_back


def test_read_empty_file(tmp_path):
    file_path = tmp_path / "empty.json"
    with open(file_path, "w") as f:
        f.write("[]")

    read_cars = read_cars_from_file(str(file_path))
    assert read_cars == []


def test_read_file_with_invalid_content(tmp_path):
    file_path = tmp_path / "invalid.json"
    with open(file_path, "w") as f:
        f.write("invalid json")

    with pytest.raises(json.JSONDecodeError):
        read_cars_from_file(str(file_path))
