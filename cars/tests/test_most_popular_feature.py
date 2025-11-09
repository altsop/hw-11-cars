import sys
import os

from cars.Car import Car, most_popular_feature

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

def test_most_popular_feature_basic():
    cars = [
        Car("BMW", "X5", 12.3, ["leather", "heated seats", "GPS"]),
        Car("BMW", "X6", 7.2, ["leather", "heated seats", "panorama", "GPS"]),
        Car("Audi", "A6", 9.93, ["leather", "heated seats", "panorama", "GPS"]),
        Car("Audi", "A7", 15.21, ["leather", "heated seats", "panorama", "sport package"]),
        Car("Mercedes", "S500", 10.6, ["leather", "panorama", "sport package", "premium sound system"]),
    ]
    result = most_popular_feature(cars)
    # The most popular feature here is "leather" (all cars have it)
    assert result == "leather"

def test_most_popular_feature_with_tie():
    cars = [
        Car("BMW", "X5", 12.3, ["leather", "heated seats"]),
        Car("BMW", "X6", 7.2, ["heated seats", "panorama"]),
        Car("Audi", "A6", 9.93, ["panorama", "GPS"]),
        Car("Audi", "A7", 15.21, ["GPS"]),
    ]
    result = most_popular_feature(cars)
    # "heated seats" and "panorama" both appear twice, so either is valid
    assert result in ["heated seats", "panorama", "GPS"]

def test_most_popular_feature_empty_cars():
    result = most_popular_feature([])
    assert result is None or result == ""

def test_most_popular_feature_single_car():
    cars = [Car("Tesla", "Model 3", 0.0, ["autopilot", "electric"])]
    result = most_popular_feature(cars)
    assert result in ["autopilot", "electric"]
