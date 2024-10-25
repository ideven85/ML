from src.average_list import add_list
import unittest


def test_average_list():
    data = [2, 4, 6, 8]
    assert add_list(data) == sum(data) / len(data)
    mock = ["A", "B", "C", "D"]
