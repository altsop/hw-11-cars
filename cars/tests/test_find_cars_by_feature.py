import sys
import os

from cars.Car import Car, find_cars_by_feature

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

def test_find_cars_with_feature():
    cars = [
        Car("BMW", "X5", 12.3, ["leather", "heated seats", "GPS"]),
        Car("BMW", "X6", 7.2, ["leather", "heated seats", "panorama", "GPS"]),
        Car("Audi", "A6", 9.93, ["leather", "heated seats", "panorama", "GPS"]),
        Car("Audi", "A7", 15.21, ["leather", "heated seats", "panorama", "sport package"]),
        Car("Mercedes", "S500", 10.6, ["leather", "panorama", "sport package", "premium sound system"]),
    ]

    result = find_cars_by_feature(cars, "panorama")
    expected = [
        Car("Audi", "A6", 9.93, ["leather", "heated seats", "panorama", "GPS"]),
        Car("Audi", "A7", 15.21, ["leather", "heated seats", "panorama", "sport package"]),
        Car("BMW", "X6", 7.2, ["leather", "heated seats", "panorama", "GPS"]),
        Car("Mercedes", "S500", 10.6, ["leather", "panorama", "sport package", "premium sound system"]),
    ]
    assert result == expected

def test_no_cars_with_feature():
    cars = [
        Car("BMW", "X5", 12.3, ["leather", "heated seats", "GPS"]),
        Car("Audi", "A6", 9.93, ["leather", "heated seats", "GPS"]),
    ]
    result = find_cars_by_feature(cars, "sunroof")
    assert result == []

def test_all_cars_with_feature():
    cars = [
        Car("BMW", "X5", 12.3, ["panorama"]),
        Car("Audi", "A6", 9.93, ["panorama"]),
        Car("Mercedes", "S500", 10.6, ["panorama"]),
    ]
    result = find_cars_by_feature(cars, "panorama")
    expected = sorted(cars, key=lambda car: (car.make, car.model))
    assert result == expected

def test_empty_car_list():
    result = find_cars_by_feature([], "panorama")
    assert result == []
