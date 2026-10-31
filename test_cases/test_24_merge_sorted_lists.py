import importlib

module = importlib.import_module("24_merge_sorted_lists")
merge_sorted_lists = module.merge_sorted_lists


def test_basic_merge():
    assert merge_sorted_lists([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]


def test_one_empty_list():
    assert merge_sorted_lists([], [1, 2]) == [1, 2]
    assert merge_sorted_lists([1, 2], []) == [1, 2]


def test_both_empty():
    assert merge_sorted_lists([], []) == []


def test_duplicates_and_negatives():
    assert merge_sorted_lists([-3, 0, 2], [-3, 2, 5]) == [-3, -3, 0, 2, 2, 5]


def test_all_of_one_list_smaller():
    assert merge_sorted_lists([1, 2], [3, 4]) == [1, 2, 3, 4]
