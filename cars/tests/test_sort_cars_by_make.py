import sys
import os

from cars.Car import Car, sort_cars_by_make

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))


def test_sort_basic():
    cars = [
        Car("BMW", "X5", 12.3, ["leather", "heated seats", "GPS"]),
        Car("BMW", "X6", 7.2, ["leather", "heated seats", "panorama", "GPS"]),
        Car("Audi", "A6", 9.93, ["leather", "heated seats", "panorama", "GPS"]),
        Car("Audi", "A7", 15.21, ["leather", "heated seats", "panorama", "sport package"]),
        Car("Mercedes", "S500", 10.6, ["leather", "panorama", "sport package", "premium sound system"]),
    ]

    sorted_cars = sort_cars_by_make(cars)
    expected_order = [
        Car("Audi", "A6", 9.93, ["leather", "heated seats", "panorama", "GPS"]),
        Car("Audi", "A7", 15.21, ["leather", "heated seats", "panorama", "sport package"]),
        Car("BMW", "X5", 12.3, ["leather", "heated seats", "GPS"]),
        Car("BMW", "X6", 7.2, ["leather", "heated seats", "panorama", "GPS"]),
        Car("Mercedes", "S500", 10.6, ["leather", "panorama", "sport package", "premium sound system"]),
    ]

    assert sorted_cars == expected_order

def test_empty_list():
    assert sort_cars_by_make([]) == []

def test_single_element():
    cars = [Car("Tesla", "Model 3", 13.0, ["autopilot", "electric"])]
    assert sort_cars_by_make(cars) == cars

def test_same_make_and_model():
    car1 = Car("Audi", "A4", 8.5, ["sunroof"])
    car2 = Car("Audi", "A4", 7.9, ["bluetooth"])
    cars = [car2, car1]
    sorted_cars = sort_cars_by_make(cars)
    # order doesn't matter for same make and model, but both should be present
    assert sorted_cars[0].make == "Audi"
    assert sorted_cars[0].model == "A4"
    assert sorted_cars[1].make == "Audi"
    assert sorted_cars[1].model == "A4"
    assert set(sorted_cars) == {car1, car2}
