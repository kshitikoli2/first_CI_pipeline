import importlib
module = importlib.import_module("26_sum_of_list")
sum_of_list = module.sum_of_list


def test_normal():
    assert sum_of_list([1, 2, 3, 4]) == 10


def test_empty():
    assert sum_of_list([]) == 0


def test_single():
    assert sum_of_list([5]) == 5


def test_negative():
    assert sum_of_list([-1, 1, -2, 2]) == 0


def test_all_negative():
    assert sum_of_list([-1, -2, -3]) == -6
