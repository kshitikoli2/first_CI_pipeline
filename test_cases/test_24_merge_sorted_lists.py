import importlib
module = importlib.import_module("24_merge_sorted_lists")
merge_sorted_lists = module.merge_sorted_lists


def test_normal():
    assert merge_sorted_lists([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]


def test_empty_first():
    assert merge_sorted_lists([], [1, 2]) == [1, 2]


def test_empty_second():
    assert merge_sorted_lists([1, 2], []) == [1, 2]


def test_duplicates():
    assert merge_sorted_lists([1, 2], [2, 3]) == [1, 2, 2, 3]


def test_both_empty():
    assert merge_sorted_lists([], []) == []
