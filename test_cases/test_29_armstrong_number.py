import importlib
module = importlib.import_module("29_armstrong_number")
is_armstrong = module.is_armstrong


def test_armstrong():
    assert is_armstrong(153) is True


def test_not_armstrong():
    assert is_armstrong(123) is False


def test_zero():
    assert is_armstrong(0) is True


def test_negative():
    assert is_armstrong(-153) is False


def test_three_digit_armstrong():
    assert is_armstrong(370) is True
