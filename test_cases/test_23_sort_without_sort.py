import importlib
module = importlib.import_module("23_sort_without_sort")
bubble_sort = module.bubble_sort


def test_normal():
    assert bubble_sort([5, 2, 9, 1]) == [1, 2, 5, 9]


def test_empty():
    assert bubble_sort([]) == []


def test_single():
    assert bubble_sort([7]) == [7]


def test_duplicates():
    assert bubble_sort([3, 2, 3, 1]) == [1, 2, 3, 3]


def test_input_is_not_mutated():
    numbers = [3, 1, 2]
    bubble_sort(numbers)
    assert numbers == [3, 1, 2]
