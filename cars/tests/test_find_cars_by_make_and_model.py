import sys
import os

from cars.Car import Car, find_cars_by_make_and_model

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

def test_find_existing_make_and_model():
    cars = [
        Car("BMW", "X5", 12.3, ["leather", "heated seats", "GPS"]),
        Car("BMW", "X6", 7.2, ["leather", "heated seats", "panorama", "GPS"]),
        Car("Audi", "A6", 9.93, ["leather", "heated seats", "panorama", "GPS"]),
    ]

    result = find_cars_by_make_and_model(cars, "BMW", "X6")
    expected = [Car("BMW", "X6", 7.2, ["leather", "heated seats", "panorama", "GPS"])]
    assert result == expected

def test_find_no_match():
    cars = [
        Car("BMW", "X5", 12.3, ["leather", "heated seats", "GPS"]),
        Car("Audi", "A6", 9.93, ["leather", "heated seats", "panorama", "GPS"]),
    ]

    result = find_cars_by_make_and_model(cars, "Mercedes", "S500")
    assert result == []

def test_find_multiple_matches():
    car1 = Car("Audi", "A4", 8.5, ["sunroof"])
    car2 = Car("Audi", "A4", 7.9, ["bluetooth"])
    cars = [car1, car2]

    result = find_cars_by_make_and_model(cars, "Audi", "A4")
    assert set(result) == {car1, car2}

def test_empty_car_list():
    result = find_cars_by_make_and_model([], "BMW", "X5")
    assert result == []
