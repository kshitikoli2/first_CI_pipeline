import importlib
module = importlib.import_module("28_set_intersection")
set_intersection = module.set_intersection


def test_normal():
    assert set_intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}


def test_no_common():
    assert set_intersection({1}, {2}) == set()


def test_same_sets():
    assert set_intersection({1, 2}, {1, 2}) == {1, 2}


def test_empty():
    assert set_intersection(set(), {1}) == set()


def test_string_elements():
    assert set_intersection({"a", "b"}, {"b", "c"}) == {"b"}
