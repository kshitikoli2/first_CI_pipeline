import importlib
module = importlib.import_module("27_rotate_list")
rotate_list = module.rotate_list


def test_right_rotation():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_large_k():
    assert rotate_list([1, 2, 3], 4) == [3, 1, 2]


def test_left_rotation():
    assert rotate_list([1, 2, 3, 4], -1) == [2, 3, 4, 1]


def test_empty():
    assert rotate_list([], 3) == []


def test_zero_rotation():
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]
