import importlib

module = importlib.import_module("23_sort_without_sort")
bubble_sort = module.bubble_sort


def test_basic_sort():
    assert bubble_sort([5, 2, 9, 1]) == [1, 2, 5, 9]


def test_original_list_not_changed():
    original = [3, 1, 2]
    bubble_sort(original)
    assert original == [3, 1, 2]


def test_empty_list():
    assert bubble_sort([]) == []


def test_single_element():
    assert bubble_sort([7]) == [7]


def test_negative_and_duplicates():
    assert bubble_sort([3, -1, 3, 0, -5]) == [-5, -1, 0, 3, 3]


def test_already_sorted():
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
