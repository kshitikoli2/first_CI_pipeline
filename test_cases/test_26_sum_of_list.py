import importlib
import pytest

module = importlib.import_module("26_sum_of_list")
sum_of_list = module.sum_of_list


def test_basic_sum():
    assert sum_of_list([1, 2, 3, 4]) == 10


def test_empty_list():
    assert sum_of_list([]) == 0


def test_single_element():
    assert sum_of_list([42]) == 42


def test_negative_numbers():
    assert sum_of_list([-5, 10, -3]) == 2


def test_decimal_numbers():
    assert sum_of_list([0.1, 0.2]) == pytest.approx(0.3)
