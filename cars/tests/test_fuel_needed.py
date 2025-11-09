import sys
import os

from cars.Car import Car, fuel_needed

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))


def test_fuel_needed_basic():
    car = Car("BMW", "X5", 12.3, ["leather", "heated seats", "GPS"])
    distance = 150  # km
    expected_fuel = (12.3 * 150) / 100  # fuel consumption is liters per 100 km
    result = fuel_needed(car, distance)
    assert result == expected_fuel

def test_fuel_needed_zero_distance():
    car = Car("Audi", "A6", 9.93, ["leather", "heated seats", "panorama", "GPS"])
    distance = 0
    expected_fuel = 0.0
    assert fuel_needed(car, distance) == expected_fuel

def test_fuel_needed_large_distance():
    car = Car("Mercedes", "S500", 10.6, ["leather", "panorama", "sport package", "premium sound system"])
    distance = 10000  # 10,000 km
    expected_fuel = (10.6 * 10000) / 100
    assert fuel_needed(car, distance) == expected_fuel

def test_fuel_needed_float_distance():
    car = Car("Tesla", "Model S", 0, ["electric"])
    distance = 123.45
    expected_fuel = 0.0
    assert fuel_needed(car, distance) == expected_fuel
