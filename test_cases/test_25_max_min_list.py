import importlib
import pytest
module = importlib.import_module("25_max_min_list")
find_max_min = module.find_max_min


def test_normal():
    assert find_max_min([4, 9, 1, 7]) == (9, 1)


def test_single():
    assert find_max_min([5]) == (5, 5)


def test_negative():
    assert find_max_min([-4, -1, -7]) == (-1, -7)


def test_empty_raises():
    with pytest.raises(ValueError):
        find_max_min([])


def test_duplicates():
    assert find_max_min([2, 2, 2]) == (2, 2)
