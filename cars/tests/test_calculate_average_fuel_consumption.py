import pytest
import sys
import os

from cars.Car import Car, calculate_average_fuel_consumption

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

def test_average_fuel_consumption_basic():
    cars = [
        Car("BMW", "X5", 12.3, ["leather", "heated seats", "GPS"]),
        Car("BMW", "X6", 7.2, ["leather", "heated seats", "panorama", "GPS"]),
        Car("Audi", "A6", 9.93, ["leather", "heated seats", "panorama", "GPS"]),
    ]
    expected_avg = (12.3 + 7.2 + 9.93) / 3
    assert calculate_average_fuel_consumption(cars) == pytest.approx(expected_avg)

def test_average_with_one_car():
    cars = [Car("Tesla", "Model 3", 0.0, ["electric"])]
    assert calculate_average_fuel_consumption(cars) == 0.0

def test_average_with_no_cars():
    cars = []
    # Expect zero or handle as per function design (assuming zero)
    assert calculate_average_fuel_consumption(cars) == 0.0

def test_average_with_varied_fuel_consumptions():
    cars = [
        Car("CarA", "Model1", 5.0, []),
        Car("CarB", "Model2", 15.0, []),
        Car("CarC", "Model3", 10.0, []),
        Car("CarD", "Model4", 20.0, []),
    ]
    expected_avg = (5.0 + 15.0 + 10.0 + 20.0) / 4
    assert calculate_average_fuel_consumption(cars) == pytest.approx(expected_avg)
